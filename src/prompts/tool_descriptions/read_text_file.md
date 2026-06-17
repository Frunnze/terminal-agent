## Description
Read the contents of a text file, either fully or within a specific line range.

## When to use
ALWAYS use this tool when the user asks to read, view, show, or inspect any text file content. Never use any other tool for reading text file content.

## Arguments
- file_path: Absolute or relative path to the file.
- start_line: Line index to start from (0-indexed, inclusive). Defaults to 0.
- end_line: Line index to stop at (0-indexed, inclusive). Pass -1 to read the entire file. Defaults to -1.

## Returns
File contents as a string, truncated to the maximum allowed length.
