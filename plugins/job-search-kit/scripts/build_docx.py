#!/usr/bin/env python3
"""Build a formatted .docx resume or cover letter from markdown.

Usage:
    python build_docx.py resume path/to/resume.md [-o out.docx] [--no-pdf]
    python build_docx.py cover  path/to/cover.md  [-o out.docx] [--no-pdf]
"""
import argparse
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.shared import Emu, RGBColor

ROOT = Path(__file__).resolve().parent.parent
RESUME_TEMPLATE = ROOT / "templates" / "resume-template.docx"
COVER_TEMPLATE = ROOT / "templates" / "cover-template.docx"

SIZE_NAME = 228600
SIZE_CONTACT = 120650
SIZE_SECTION = 152400
SIZE_COMPANY = 139700
SIZE_BODY = 127000
RIGHT_TAB_POS = 8784

COVER_NAME = 177800
COVER_CONTACT = 127000
COVER_BODY = 139700

EM_DASH = "\u2014"

JOB_RE = re.compile(r"^\*\*(.+?)\*\*\s*\|\s*(.+)$")
BULLET_RE = re.compile(r"^[-*]\s+(.+)$")
HR_RE = re.compile(r"[-_*]{3,}")
UNSUPPORTED_RE = re.compile(r"^(#{5,}|#\S|\||>|\d+\.\s)")
INLINE_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
PDF_PAGE_RE = re.compile(rb"/Type\s*/Page(?!s)")


def parse_resume(text):
    """Parse resume markdown. Returns (blocks, warnings); blocks are (kind, data)."""
    blocks, warnings = [], []
    expect_contact = False
    for n, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        if EM_DASH in line:
            warnings.append(f"line {n}: em dash found, rewrite without it")
        if expect_contact and not line.startswith("#"):
            blocks.append(("contact", line))
            expect_contact = False
            continue
        expect_contact = False
        if line.startswith("# "):
            blocks.append(("name", line[2:].strip()))
            expect_contact = True
        elif line.startswith("## "):
            blocks.append(("section", line[3:].strip()))
        elif line.startswith("### "):
            name, _, desc = line[4:].partition("|")
            blocks.append(("company", (name.strip(), desc.strip() or None)))
        elif line.startswith("#### "):
            blocks.append(("subheader", line[5:].strip()))
        elif HR_RE.fullmatch(line):
            warnings.append(f"line {n}: horizontal rule ignored")
        elif m := BULLET_RE.match(line):
            blocks.append(("bullet", m.group(1).strip()))
        elif m := JOB_RE.match(line):
            blocks.append(("job", (m.group(1).strip(), m.group(2).strip())))
        elif UNSUPPORTED_RE.match(line):
            warnings.append(f"line {n}: unsupported markdown rendered as plain text: {line[:50]}")
            blocks.append(("body", line.lstrip("#>|").strip()))
        else:
            blocks.append(("body", line))
    return blocks, warnings


def _clear_body(doc):
    body = doc.element.body
    for child in list(body):
        if not child.tag.endswith("}sectPr"):
            body.remove(child)


def _add_text(p, text, size, bold=False, italic=False):
    """Add text to paragraph p, honoring **inline bold**."""
    for i, part in enumerate(INLINE_BOLD_RE.split(text)):
        if not part:
            continue
        run = p.add_run(part)
        run.font.size = Emu(size)
        if bold or i % 2 == 1:
            run.bold = True
        if italic:
            run.italic = True
    return p


def render_resume(blocks, out_path, template=RESUME_TEMPLATE):
    doc = Document(str(template))
    _clear_body(doc)
    for kind, data in blocks:
        if kind == "name":
            p = _add_text(doc.add_paragraph(), data, SIZE_NAME, bold=True)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif kind == "contact":
            p = _add_text(doc.add_paragraph(), data, SIZE_CONTACT)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif kind == "section":
            doc.add_paragraph()
            p = _add_text(doc.add_paragraph(), data, SIZE_SECTION, bold=True)
            for r in p.runs:
                r.font.color.rgb = RGBColor(0, 0, 0)
            p._element.get_or_add_pPr().append(
                parse_xml('<w:spacing {} w:before="80" w:after="80"/>'.format(nsdecls("w")))
            )
        elif kind == "company":
            name, desc = data
            p = _add_text(doc.add_paragraph(), name, SIZE_COMPANY, bold=True)
            if desc:
                _add_text(p, f" ({desc})", SIZE_BODY, italic=True)
        elif kind == "job":
            title, dates = data
            p = _add_text(doc.add_paragraph(), title, SIZE_BODY, bold=True)
            _add_text(p, f"\t{dates}", SIZE_BODY)
            p._element.get_or_add_pPr().append(parse_xml(
                '<w:tabs {}><w:tab w:pos="{}" w:val="right"/></w:tabs>'.format(nsdecls("w"), RIGHT_TAB_POS)
            ))
        elif kind == "subheader":
            _add_text(doc.add_paragraph(), data, SIZE_BODY, bold=True, italic=True)
        elif kind == "bullet":
            _add_text(doc.add_paragraph(style="List Bullet"), data, SIZE_BODY)
        else:
            _add_text(doc.add_paragraph(), data, SIZE_BODY)
    doc.save(str(out_path))
    return out_path


def parse_cover(text):
    blocks, warnings = [], []
    expect_contact = False
    for n, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        if EM_DASH in line:
            warnings.append(f"line {n}: em dash found, rewrite without it")
        if line.startswith("# "):
            blocks.append(("name", line[2:].strip()))
            expect_contact = True
            continue
        if expect_contact:
            blocks.append(("contact", line))
            expect_contact = False
            continue
        if line.startswith("#"):
            warnings.append(f"line {n}: headings are not used in cover letters, rendered as text")
            line = line.lstrip("#").strip()
        blocks.append(("body", line))
    return blocks, warnings


def render_cover(blocks, out_path, template=COVER_TEMPLATE):
    doc = Document(str(template))
    _clear_body(doc)
    sizes = {"name": COVER_NAME, "contact": COVER_CONTACT}
    for kind, data in blocks:
        _add_text(doc.add_paragraph(), data, sizes.get(kind, COVER_BODY), bold=(kind == "name"))
    doc.save(str(out_path))
    return out_path


def estimate_pages(blocks, chars_per_line=100, lines_per_page=52):
    lines = 0
    for kind, data in blocks:
        text = data if isinstance(data, str) else " ".join(x for x in data if x)
        lines += max(1, math.ceil(len(text) / chars_per_line))
        if kind == "section":
            lines += 2
    return lines / lines_per_page


def export_pdf(docx_path):
    """Convert with LibreOffice if installed. Returns the PDF path or None."""
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        return None
    docx_path = Path(docx_path)
    try:
        subprocess.run(
            [soffice, "--headless", "--convert-to", "pdf", "--outdir", str(docx_path.parent), str(docx_path)],
            check=True, capture_output=True, timeout=120,
        )
    except (subprocess.SubprocessError, OSError):
        return None
    pdf = docx_path.with_suffix(".pdf")
    return pdf if pdf.exists() else None


def count_pdf_pages(pdf_path):
    return len(PDF_PAGE_RE.findall(Path(pdf_path).read_bytes()))


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build a .docx resume or cover letter from markdown.")
    ap.add_argument("kind", choices=["resume", "cover"])
    ap.add_argument("source", type=Path)
    ap.add_argument("-o", "--output", type=Path)
    ap.add_argument("--no-pdf", action="store_true", help="skip PDF export")
    args = ap.parse_args(argv)

    text = args.source.read_text(encoding="utf-8")
    out = args.output or args.source.with_suffix(".docx")
    if args.kind == "resume":
        blocks, warnings = parse_resume(text)
        render_resume(blocks, out)
    else:
        blocks, warnings = parse_cover(text)
        render_cover(blocks, out)

    for w in warnings:
        print(f"WARNING: {w}")
    print(f"Wrote {out}")
    pdf = None if args.no_pdf else export_pdf(out)
    if pdf:
        print(f"Wrote {pdf} ({count_pdf_pages(pdf)} pages)")
    else:
        print(f"Estimated length: {estimate_pages(blocks):.1f} pages "
              "(install LibreOffice for PDF export and an exact page count)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
