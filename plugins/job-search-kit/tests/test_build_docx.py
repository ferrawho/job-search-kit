import sys
from pathlib import Path

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
