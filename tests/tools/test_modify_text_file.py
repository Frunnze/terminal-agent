import os
import tempfile


from src.tools.modify_text_file import TextFileModifierTool


class _MockEmitter:
    def __init__(self):
        self.lines = []

    def emit(self, text):
        self.lines.append(text)


def _tool():
    return TextFileModifierTool(_MockEmitter()).modify_text_file


def _write_tmp(content: str) -> str:
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
    f.write(content)
    f.close()
    return f.name


def test_overwrite_full_file():
    path = _write_tmp("old content")
    try:
        result = _tool().invoke(
            {"file_path": path, "new_content": "new content"}
        )
        assert result == "ok"
        with open(path) as f:
            assert f.read() == "new content\n"
    finally:
        os.unlink(path)


def test_replace_line_range():
    path = _write_tmp("line0\nline1\nline2\nline3\n")
    try:
        result = _tool().invoke(
            {"file_path": path, "new_content": "replaced", "start_line": 1, "end_line": 2}
        )
        assert result == "ok"
        with open(path) as f:
            lines = f.read().splitlines()
        assert lines == ["line0", "replaced", "line3"]
    finally:
        os.unlink(path)


def test_replace_single_line():
    path = _write_tmp("line0\nline1\nline2\n")
    try:
        _tool().invoke(
            {"file_path": path, "new_content": "changed", "start_line": 1, "end_line": 1}
        )
        with open(path) as f:
            lines = f.read().splitlines()
        assert lines == ["line0", "changed", "line2"]
    finally:
        os.unlink(path)


def test_returns_error_on_missing_file():
    result = _tool().invoke(
        {"file_path": "/nonexistent/path/file.txt", "new_content": "x"}
    )
    assert result.startswith("Error modifying file:")


def test_overwrite_creates_empty_file():
    path = _write_tmp("some content")
    try:
        _tool().invoke(
            {"file_path": path, "new_content": ""}
        )
        with open(path) as f:
            assert f.read() == ""
    finally:
        os.unlink(path)


def test_replace_with_trailing_newline_in_replacement():
    path = _write_tmp("a\nb\nc\n")
    try:
        result = _tool().invoke(
            {"file_path": path, "new_content": "x\n", "start_line": 1, "end_line": 1}
        )
        assert result == "ok"
        with open(path) as f:
            assert f.read() == "a\nx\nc\n"
    finally:
        os.unlink(path)
