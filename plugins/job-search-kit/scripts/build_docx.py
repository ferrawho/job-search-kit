#!/usr/bin/env python3
"""Build a formatted .docx resume or cover letter from markdown.

Usage:
    python build_docx.py resume path/to/resume.md [-o out.docx] [--no-pdf]
    python build_docx.py cover  path/to/cover.md  [-o out.docx] [--no-pdf]
"""
import re

EM_DASH = "\u2014"

JOB_RE = re.compile(r"^\*\*(.+?)\*\*\s*\|\s*(.+)$")
BULLET_RE = re.compile(r"^[-*]\s+(.+)$")
HR_RE = re.compile(r"[-_*]{3,}")
UNSUPPORTED_RE = re.compile(r"^(#{5,}|#\S|\||>|\d+\.\s)")
INLINE_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


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
