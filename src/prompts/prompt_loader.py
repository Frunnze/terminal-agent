from pathlib import Path

from langchain_core.prompts import PromptTemplate

from interfaces.prompt_loader import IPromptLoader

_PROMPTS_DIR = Path(__file__).parent
_TOOL_DESCRIPTIONS_DIR = _PROMPTS_DIR / "tool_descriptions"
_AGENT_RULES_PATH = Path(__file__).parent.parent.parent / "AGENTS.md"


class PromptLoader(IPromptLoader):
    def load_system_prompt(self) -> str:
        """Load and render the system prompt with agent rules injected.

        Returns:
            Rendered system prompt string.
        """
        template = (_PROMPTS_DIR / "system_prompt.md").read_text()
        agent_rules = _AGENT_RULES_PATH.read_text()

        return PromptTemplate.from_template(template).format(
            agent_rules=agent_rules
        )

    def load_tool_description(self, tool_name: str) -> str:
        """Load a tool description from the tool_descriptions directory.

        Args:
            tool_name: Name of the tool, matching its .md filename.

        Returns:
            Tool description string.
        """
        return (_TOOL_DESCRIPTIONS_DIR / f"{tool_name}.md").read_text()
