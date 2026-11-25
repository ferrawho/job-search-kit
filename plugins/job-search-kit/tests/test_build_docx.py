import sys
from pathlib import Path

import pytest
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import build_docx as b  # noqa: E402

SAMPLE = """# SAM RIVERA
Springfield, IL | sam@example.com | linkedin.com/in/example

## SUMMARY
Operations analyst with **8 years** of experience.

## EXPERIENCE
### Acme Corp | Logistics, 200 employees
**Operations Analyst** | Jan 2020 \u2013 Present
#### Reporting:
- Cut weekly report time by 50%

## EDUCATION
**BSc Economics**, State University, 2015
"""


def kinds(blocks):
    return [k for k, _ in blocks]


def warns(text):
    """Resume warnings minus the no-name warning, for fragment tests."""
    return [w for w in b.parse_resume(text)[1] if "no '# Name'" not in w]


def test_parse_resume_kinds():
    blocks, warnings = b.parse_resume(SAMPLE)
    assert kinds(blocks) == [
        "name", "contact", "section", "body", "section", "company",
        "job", "subheader", "bullet", "section", "body",
    ]
    assert warnings == []


def test_company_with_and_without_description():
    blocks, _ = b.parse_resume("### Acme Corp | Logistics\n### Solo Inc.\n")
    assert blocks == [("company", ("Acme Corp", "Logistics")), ("company", ("Solo Inc.", None))]


def test_job_line():
    blocks, _ = b.parse_resume("**Operations Analyst** | Jan 2020 - Present\n")
    assert blocks == [("job", ("Operations Analyst", "Jan 2020 - Present"))]


def test_unsupported_markdown_warns_and_renders_as_body():
    blocks, _ = b.parse_resume("| a | b |\n##### deep\n> quote\n1. item\n")
    warnings = warns("| a | b |\n##### deep\n> quote\n1. item\n")
    assert len(warnings) == 4
    assert all(w.startswith("line ") for w in warnings)
    assert kinds(blocks) == ["body"] * 4


def test_em_dash_warns():
    warnings = warns("- Did a thing \u2014 well\n")
    assert len(warnings) == 1 and "em dash" in warnings[0]


def test_horizontal_rule_ignored_with_warning():
    blocks, _ = b.parse_resume("---\n")
    assert blocks == [] and len(warns("---\n")) == 1


def render_sample(tmp_path):
    blocks, _ = b.parse_resume(SAMPLE)
    out = tmp_path / "resume.docx"
    b.render_resume(blocks, out)
    return Document(str(out))


def test_render_resume_paragraph_sequence(tmp_path):
    doc = render_sample(tmp_path)
    texts = [p.text for p in doc.paragraphs]
    assert texts == [
        "SAM RIVERA",
        "Springfield, IL | sam@example.com | linkedin.com/in/example",
        "", "SUMMARY",
        "Operations analyst with 8 years of experience.",
        "", "EXPERIENCE",
        "Acme Corp (Logistics, 200 employees)",
        "Operations Analyst\tJan 2020 \u2013 Present",
        "Reporting:",
        "Cut weekly report time by 50%",
        "", "EDUCATION",
        "BSc Economics, State University, 2015",
    ]


def test_render_resume_formatting(tmp_path):
    doc = render_sample(tmp_path)
    p = doc.paragraphs
    assert p[0].alignment == WD_ALIGN_PARAGRAPH.CENTER and p[0].runs[0].bold
    assert p[10].style.name == "List Bullet"
    sec = Document(str(b.RESUME_TEMPLATE)).sections[-1]
    width = (sec.page_width - sec.left_margin - sec.right_margin) // 635
    assert width == 10224
    assert 'w:pos="{}"'.format(width) in p[8]._element.xml
    bold_runs = [r.text for r in p[4].runs if r.bold]
    assert bold_runs == ["8 years"]
    assert p[7].runs[1].italic


COVER = """# Sam Rivera
Springfield, IL | sam@example.com

November 25, 2026

Dear Hiring Team,

I run **weekly ops reporting** for a 200-person logistics team.

Best regards,
Sam Rivera
"""


def test_parse_cover():
    blocks, warnings = b.parse_cover(COVER)
    assert kinds(blocks) == ["name", "contact", "body", "body", "body", "body", "body"]
    assert warnings == []


def test_render_cover(tmp_path):
    blocks, _ = b.parse_cover(COVER)
    out = tmp_path / "cover.docx"
    b.render_cover(blocks, out)
    doc = Document(str(out))
    assert [p.text for p in doc.paragraphs][0:2] == ["Sam Rivera", "Springfield, IL | sam@example.com"]
    assert doc.paragraphs[0].runs[0].bold
    assert [r.text for r in doc.paragraphs[4].runs if r.bold] == ["weekly ops reporting"]


def test_estimate_pages_grows_with_content():
    small, _ = b.parse_resume(SAMPLE)
    big, _ = b.parse_resume(SAMPLE + "\n".join(["- " + "x" * 150] * 80))
    assert 0 < b.estimate_pages(small) < 1 < b.estimate_pages(big)


def test_count_pdf_pages(tmp_path):
    pdf = tmp_path / "x.pdf"
    pdf.write_bytes(b"<< /Type /Pages /Kids [] >> << /Type /Page >> << /Type/Page >>")
    assert b.count_pdf_pages(pdf) == 2


def test_cli_builds_resume(tmp_path, capsys):
    src = tmp_path / "resume.md"
    src.write_text(SAMPLE + "- bad \u2014 dash\n", encoding="utf-8")
    assert b.main(["resume", str(src), "--no-pdf"]) == 0
    assert (tmp_path / "resume.docx").exists()
    out = capsys.readouterr().out
    assert "WARNING: line" in out and "Estimated length" in out


def test_cli_output_flag(tmp_path):
    src = tmp_path / "cover.md"
    src.write_text(COVER, encoding="utf-8")
    dst = tmp_path / "Sam-Rivera-Cover.docx"
    assert b.main(["cover", str(src), "-o", str(dst), "--no-pdf"]) == 0
    assert dst.exists()


# --- review findings ---

def test_cli_survives_cp1252_stdout(tmp_path, monkeypatch):
    import io
    monkeypatch.setattr(sys, "stdout", io.TextIOWrapper(io.BytesIO(), encoding="cp1252"))
    src = tmp_path / "resume.md"
    src.write_text("# Sam\nCity | e\n> quote \u2192 x\n", encoding="utf-8")
    assert b.main(["resume", str(src), "--no-pdf"]) == 0


def test_parse_strips_bom():
    blocks, _ = b.parse_resume("\ufeff# Sam\nCity | e\n")
    assert blocks == [("name", "Sam"), ("contact", "City | e")]
    blocks, _ = b.parse_cover("\ufeff# Sam\nCity | e\n")
    assert blocks == [("name", "Sam"), ("contact", "City | e")]


def test_cli_reads_bom_file(tmp_path):
    src = tmp_path / "resume.md"
    src.write_bytes("\ufeff# Sam\nCity | e\n".encode("utf-8"))
    assert b.main(["resume", str(src), "--no-pdf"]) == 0
    assert Document(str(tmp_path / "resume.docx")).paragraphs[0].text == "Sam"


def test_find_soffice_env_var_wins(tmp_path, monkeypatch):
    exe = tmp_path / "soffice.exe"
    exe.write_text("")
    monkeypatch.setenv("SOFFICE", str(exe))
    monkeypatch.setattr(b.shutil, "which", lambda name: "/usr/bin/" + name)
    assert b.find_soffice() == str(exe)


def test_find_soffice_known_path(tmp_path, monkeypatch):
    exe = tmp_path / "soffice.exe"
    exe.write_text("")
    monkeypatch.delenv("SOFFICE", raising=False)
    monkeypatch.setattr(b.shutil, "which", lambda name: None)
    monkeypatch.setattr(b, "SOFFICE_CANDIDATES", [str(tmp_path / "missing.exe"), str(exe)])
    assert b.find_soffice() == str(exe)


def test_find_soffice_none(tmp_path, monkeypatch):
    monkeypatch.delenv("SOFFICE", raising=False)
    monkeypatch.setattr(b.shutil, "which", lambda name: None)
    monkeypatch.setattr(b, "SOFFICE_CANDIDATES", [str(tmp_path / "missing.exe")])
    assert b.find_soffice() is None


def test_export_pdf_removes_stale_pdf(tmp_path, monkeypatch):
    monkeypatch.setattr(b, "find_soffice", lambda: "soffice")
    monkeypatch.setattr(b.subprocess, "run", lambda *a, **k: None)
    docx = tmp_path / "x.docx"
    docx.write_bytes(b"")
    stale = tmp_path / "x.pdf"
    stale.write_bytes(b"old")
    assert b.export_pdf(docx) is None
    assert not stale.exists()


def test_cli_missing_source(tmp_path, capsys):
    missing = tmp_path / "nope.md"
    assert b.main(["resume", str(missing), "--no-pdf"]) == 1
    assert f"ERROR: can't find {missing}" in capsys.readouterr().out


def test_cli_creates_output_folder(tmp_path):
    src = tmp_path / "cover.md"
    src.write_text(COVER, encoding="utf-8")
    dst = tmp_path / "new" / "sub" / "cover.docx"
    assert b.main(["cover", str(src), "-o", str(dst), "--no-pdf"]) == 0
    assert dst.exists()


def test_cli_permission_error(tmp_path, monkeypatch, capsys):
    src = tmp_path / "resume.md"
    src.write_text(SAMPLE, encoding="utf-8")

    def boom(*a, **k):
        raise PermissionError("locked")

    monkeypatch.setattr(b, "render_resume", boom)
    assert b.main(["resume", str(src), "--no-pdf"]) == 1
    out = capsys.readouterr().out
    assert "ERROR: can't write" in out and "close it and run again" in out


def test_missing_contact_line_warns():
    blocks, warnings = b.parse_resume("# Sam\n- Built things\n## SKILLS\n")
    assert blocks == [("name", "Sam"), ("bullet", "Built things"), ("section", "SKILLS")]
    assert warnings == ["line 2: no contact line after name"]
    blocks, warnings = b.parse_resume("# Sam\n**Analyst** | 2020\n")
    assert kinds(blocks) == ["name", "job"] and len(warnings) == 1
    blocks, warnings = b.parse_resume("# Sam\n---\n")
    assert kinds(blocks) == ["name"] and "no contact line" in warnings[0]


def test_stray_asterisks_warn():
    assert warns("- Built **things\n") == ["line 1: stray * (unclosed bold or *italic*), check formatting"]
    assert warns("Some *italic* text\n") == ["line 1: stray * (unclosed bold or *italic*), check formatting"]
    assert warns("- Built **many** things\n") == []


def test_count_pdf_pages_ignores_page_label(tmp_path):
    pdf = tmp_path / "x.pdf"
    pdf.write_bytes(b"<< /Type /Page >> << /Type /PageLabel >> << /Type /Pages >>")
    assert b.count_pdf_pages(pdf) == 1


def test_cli_output_without_extension(tmp_path):
    src = tmp_path / "cover.md"
    src.write_text(COVER, encoding="utf-8")
    assert b.main(["cover", str(src), "-o", str(tmp_path / "Sam-Cover"), "--no-pdf"]) == 0
    assert (tmp_path / "Sam-Cover.docx").exists()


# --- Fable review ---

def test_markdown_leakage_warns_with_line_numbers():
    text = ("# Sam\nCity | e\n- See [site](http://x.com)\n- Used `SQL`\n"
            "- Very _important_ work\n+ plus bullet\n\u2022 dot bullet\nok <!-- note -->\n")
    _, warnings = b.parse_resume(text)
    assert [w.split(":")[0] for w in warnings] == ["line 3", "line 4", "line 5", "line 6", "line 7", "line 8"]
    joined = " ".join(warnings)
    for word in ("link", "backtick", "comment", "italic", "bullet"):
        assert word in joined


def test_snake_case_is_not_italic():
    assert warns("- Built file_name_parser for sam_rivera\n") == []


def test_no_name_warns():
    _, warnings = b.parse_resume("## SKILLS\n- Excel\n")
    assert warnings == ["no '# Name' line found"]


def test_comment_after_name_is_skipped_not_contact():
    blocks, warnings = b.parse_resume("# Sam\n<!-- fill this in -->\nCity | e\n")
    assert blocks == [("name", "Sam"), ("contact", "City | e")]
    assert len(warnings) == 1 and "line 2" in warnings[0] and "comment" in warnings[0]


def test_multiline_comment_skipped():
    blocks, warnings = b.parse_resume("# Sam\nCity | e\n<!--\nhidden\n-->\n- Real\n")
    assert blocks == [("name", "Sam"), ("contact", "City | e"), ("bullet", "Real")]
    assert len(warnings) == 1


def test_cover_warnings():
    text = (COVER + "<!-- tip -->\nSee [site](http://x.com) and `code`.\n"
            "- a bullet\n---\nA *loose star.\n")
    blocks, warnings = b.parse_cover(text)
    assert len(warnings) == 6 and all(w.startswith("line ") for w in warnings)
    assert all("tip" not in d and d != "---" for _, d in blocks)
    blocks, _ = b.parse_cover("# Sam\n<!-- x -->\nCity | e\n")
    assert blocks == [("name", "Sam"), ("contact", "City | e")]


def test_cli_estimate_message(tmp_path, capsys):
    src = tmp_path / "resume.md"
    src.write_text(SAMPLE, encoding="utf-8")
    assert b.main(["resume", str(src), "--no-pdf"]) == 0
    out = capsys.readouterr().out
    assert "Estimated length: about " in out and "(estimate only, open the file to confirm)" in out


def test_cli_zero_pdf_pages_falls_back_to_estimate(tmp_path, monkeypatch, capsys):
    src = tmp_path / "resume.md"
    src.write_text(SAMPLE, encoding="utf-8")
    pdf = tmp_path / "resume.pdf"
    monkeypatch.setattr(b, "export_pdf", lambda p: pdf.write_bytes(b"not a pdf") and pdf)
    assert b.main(["resume", str(src)]) == 0
    out = capsys.readouterr().out
    assert "(0 pages)" not in out
    assert "Estimated length: about" in out


def test_cli_check(monkeypatch, capsys):
    monkeypatch.setattr(b, "find_soffice", lambda: None)
    assert b.main(["--check"]) == 0
    out = capsys.readouterr().out
    assert "Python" in out and "python-docx" in out and "not found (optional)" in out
    monkeypatch.setattr(b, "find_soffice", lambda: "C:/LO/soffice.exe")
    assert b.main(["--check"]) == 0
    assert "C:/LO/soffice.exe" in capsys.readouterr().out


def test_cli_still_requires_args(capsys):
    for argv in ([], ["resume"]):
        with pytest.raises(SystemExit) as e:
            b.main(argv)
        assert e.value.code == 2
        assert "required" in capsys.readouterr().err
