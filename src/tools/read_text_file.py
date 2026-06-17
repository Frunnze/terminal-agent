from pathlib import Path

from langchain.tools import BaseTool

from config import MAX_RETURNED_CHARS

_DESCRIPTION_PATH = (
    Path(__file__).parent.parent
    / "prompts"
    / "tool_descriptions"
    / "read_text_file.md"
)


class TextFileReaderTool(BaseTool):
    name: str = "read_text_file"
    description: str = _DESCRIPTION_PATH.read_text()

    def _run(
        self,
        file_path: str,
        start_line: int = 0,
        end_line: int = -1,
    ) -> str:
        """Read a text file fully or within a line range.

        Args:
            file_path: Absolute or relative path to the file.
            start_line: Line index to start from (0-indexed, inclusive).
            end_line: Line index to stop at (0-indexed, inclusive).
                Pass -1 to read the entire file.

        Returns:
            File contents as a string, truncated to MAX_RETURNED_CHARS.
        """
        try:
            with open(file_path, "r") as file_handle:
                all_lines = file_handle.readlines()

            if start_line >= 0 and end_line >= 0 and end_line >= start_line:
                selected_lines = all_lines[start_line:end_line + 1]
                return "\n".join(selected_lines)[:MAX_RETURNED_CHARS]

            return "".join(all_lines)[:MAX_RETURNED_CHARS]
        except Exception as e:
            return f"Error reading file: {e}"
