from src.tools.read_text_file import TextFileReaderTool
from src.config import MAX_RETURNED_CHARS


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


def test_reads_line_range(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("line0\nline1\nline2\nline3\n")

    result = TextFileReaderTool.read_text_file.invoke(
        {"file_path": str(file_path), "start_line": 1, "end_line": 2}
    )
    assert "line1" in result
    assert "line2" in result
    assert "line0" not in result
    assert "line3" not in result


def test_truncates_at_max_chars(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("x" * (MAX_RETURNED_CHARS + 1000))

    result = TextFileReaderTool.read_text_file.invoke({"file_path": str(file_path)})
    assert len(result) <= MAX_RETURNED_CHARS


def test_reads_empty_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("")

    result = TextFileReaderTool.read_text_file.invoke({"file_path": str(file_path)})
    assert result == ""
