import os
import tempfile
import pytest

from src.tools.file_reader.file_reader import FileReaderTool
from src.config import MAX_RETURNED_CHARS


def _write_tmp(content: str) -> str:
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
    f.write(content)
    f.close()
    return f.name


def test_reads_full_file():
    path = _write_tmp("hello\nworld\n")
    try:
        result = FileReaderTool.read_text_file.invoke({"file_path": path})
        assert "hello" in result
        assert "world" in result
    finally:
        os.unlink(path)


def test_reads_line_range():
    path = _write_tmp("line0\nline1\nline2\nline3\n")
    try:
        result = FileReaderTool.read_text_file.invoke(
            {"file_path": path, "start_line": 1, "end_line": 2}
        )
        assert "line1" in result
        assert "line2" in result
        assert "line0" not in result
        assert "line3" not in result
    finally:
        os.unlink(path)


def test_returns_error_on_missing_file():
    result = FileReaderTool.read_text_file.invoke({"file_path": "/nonexistent/path/file.txt"})
    assert result.startswith("Error reading file:")


def test_truncates_at_max_chars():
    content = "x" * (MAX_RETURNED_CHARS + 1000)
    path = _write_tmp(content)
    try:
        result = FileReaderTool.read_text_file.invoke({"file_path": path})
        assert len(result) <= MAX_RETURNED_CHARS
    finally:
        os.unlink(path)


def test_reads_empty_file():
    path = _write_tmp("")
    try:
        result = FileReaderTool.read_text_file.invoke({"file_path": path})
        assert result == ""
    finally:
        os.unlink(path)
