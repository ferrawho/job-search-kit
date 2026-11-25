import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))
import build_docx as b  # noqa: E402


def test_fixture_master_resume_parses_clean(tmp_path):
    text = (HERE / "fixtures/sam-rivera/profile/master-resume.md").read_text(encoding="utf-8")
    blocks, warnings = b.parse_resume(text)
    assert warnings == []
    b.render_resume(blocks, tmp_path / "out.docx")
    assert (tmp_path / "out.docx").exists()
