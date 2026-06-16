from langchain.tools import tool


MAX_RETURNED_CHARS = 5000


class FileReaderTool:
    @staticmethod
    @tool
    def read(
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

        if start_line >= 0 and end_line >= 0 and end_line >= start_line:
            with open(file_path, 'r') as file:
                lines = file.readlines()[start_line:end_line+1]
            return "\n".join(lines)[:MAX_RETURNED_CHARS]
        else:
            with open(file_path, 'r') as file:
                return file.read()[:MAX_RETURNED_CHARS]
        
        return "Error reading file."