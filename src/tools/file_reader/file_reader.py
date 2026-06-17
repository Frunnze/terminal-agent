from langchain.tools import tool

from src.config import MAX_RETURNED_CHARS


class FileReaderTool:
    @staticmethod
    @tool
    def read_text_file(
        file_path: str, 
        start_line: int = 0, 
        end_line: int = -1
    ) -> str:
        """Read a file using the file path given by the user.

        Args:
            file_path: Absolute or relative path to the file.
            start_line: Line index to start from (0-indexed, inclusive).
                Defaults to 0.
            end_line: Line index to stop at (0-indexed, inclusive).
                Pass -1 to read the entire file.

        Returns:
            File contents as a string. When a line range is given,
            lines are concatenated.
        """

        try:
            if start_line >= 0 and end_line >= 0 and end_line >= start_line:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    if start_line < len(lines):
                        return "\n".join(lines[start_line:end_line + 1])[:MAX_RETURNED_CHARS]

            with open(file_path, 'r') as file:
                return file.read()[:MAX_RETURNED_CHARS]
        except Exception as e:
            return f"Error reading file: {e}"