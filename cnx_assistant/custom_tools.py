import logging
import google.cloud.logging

from google.adk.tools.tool_context import ToolContext


def add_prompt_to_state(tool_context: ToolContext, prompt: str) -> dict[str, str]:
    """Save the user's initial prompt to the state."""
    tool_context.state["PROMPT"] = prompt
    logging.info(f"[State updated] Added to PROMPT: {prompt}")
    return {"status": "sucess"}
