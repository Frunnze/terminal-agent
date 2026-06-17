## Description
Modify a text file by replacing a specific line range.

## When to use
ALWAYS use this tool when the user asks to change, update, replace, or rewrite any content in a text file — whether it is a single line, a range of lines, or the entire file. Never use any other tool for modifying text file content.

## Arguments
- file_path: absolute or relative path to the file.
- new_content: only the new lines that replace the targeted range - do not include surrounding unchanged lines. Preserve original formatting, do not add extra blank lines.
- start_line: First line to replace (0-indexed, inclusive). Defaults to 0.
- end_line: Last line to replace (0-indexed, inclusive). Must match the range of lines you want replaced — do not extend it to include unchanged context lines. Pass -1 to replace until end of file. Defaults to -1.

## Returns
"ok" on success, or an error message string.
