from langchain.tools import tool


class TextFileModifierTool:
    def __init__(self, emitter):
        self.emitter = emitter

        @tool
        def modify_text_file(
            file_path: str,
            new_content: str,
            start_line: int = 0,
            end_line: int = -1,
        ) -> str:
            """Modify a text file by replacing its full content or a specific line range.

            Args:
                file_path: Absolute or relative path to the file.
                new_content: The text to write. Replaces the whole file or the
                    specified line range.
                start_line: First line to replace (0-indexed, inclusive). Defaults to 0.
                end_line: Last line to replace (0-indexed, inclusive).
                    Pass -1 to replace until the end of the file. Defaults to -1.

            Returns:
                "ok" on success, or an error message string.
            """
            try:
                with open(file_path, 'r') as f:
                    lines = f.readlines()

                if end_line == -1:
                    end_line = len(lines) - 1

                removed = lines[start_line:end_line + 1]
                replacement_lines = [
                    l if l.endswith('\n') else l + '\n'
                    for l in new_content.splitlines()
                ]

                for l in removed:
                    emitter.emit(f"- {l.rstrip()}")
                for l in replacement_lines:
                    emitter.emit(f"+ {l.rstrip()}")

                lines[start_line:end_line + 1] = replacement_lines

                with open(file_path, 'w') as f:
                    f.writelines(lines)

                return "ok"
            except Exception as e:
                return f"Error modifying file: {e}"

        self.modify_text_file = modify_text_file
