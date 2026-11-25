import sys
from pathlib import Path

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
    blocks, warnings = b.parse_resume("| a | b |\n##### deep\n> quote\n1. item\n")
    assert len(warnings) == 4
    assert all(w.startswith("line ") for w in warnings)
    assert kinds(blocks) == ["body"] * 4


def test_em_dash_warns():
    _, warnings = b.parse_resume("- Did a thing \u2014 well\n")
    assert len(warnings) == 1 and "em dash" in warnings[0]


def test_horizontal_rule_ignored_with_warning():
    blocks, warnings = b.parse_resume("---\n")
    assert blocks == [] and len(warnings) == 1


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
    assert 'w:pos="8784"' in p[8]._element.xml
    bold_runs = [r.text for r in p[4].runs if r.bold]
    assert bold_runs == ["8 years"]
    assert p[7].runs[1].italic
