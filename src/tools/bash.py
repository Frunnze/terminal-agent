import subprocess
from langchain.tools import tool


class BashTool:
    @staticmethod
    @tool
    def run(command: str) -> str:
        """Execute a bash command."""
        
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        output_str = ""
        if result.stdout:
            output_str = f"Command output: ```{result.stdout}```."
        
        if result.stderr:
            output_str += f"Command error: ```{result.stderr}```."

        return output_str