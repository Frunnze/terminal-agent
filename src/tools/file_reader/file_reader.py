from langchain.tools import tool


class FileReaderTool:
    @staticmethod
    @tool
    def read(file_path: str) -> str:
        """Read a file using the file path given by the user."""
        with open(file_path, 'r') as file:
            return file.read()