import os
import sys

# Ensure `src` and the repo root are importable when running tests.
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
SRC_ROOT = os.path.join(REPO_ROOT, "src")
sys.path.extend([REPO_ROOT, SRC_ROOT])

from src.tools.read_text_file import TextFileReaderTool


def test_read_existing_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("hello")

    result = TextFileReaderTool.read_text_file.invoke({"file_path": str(file_path)})
    assert result == "hello"


def test_returns_error_on_missing_file():
    result = TextFileReaderTool.read_text_file.invoke(
        {"file_path": "/nonexistent/path/file.txt"}
    )
    assert result.startswith("Error reading file:")
