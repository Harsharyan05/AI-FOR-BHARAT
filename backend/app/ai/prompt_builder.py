"""
Prompt Builder

Builds prompts for LLMs using retrieved repository context.

Author: Harsh Aryan
Project: Cognisys
"""

from typing import List


class PromptBuilder:
    """
    Builds structured prompts for repository reasoning.
    """

    SYSTEM_PROMPT = """
You are Cognisys AI.

You are an expert Software Architect, Senior Backend Engineer,
DevOps Engineer and Code Reviewer.

Your job is to answer ONLY using the repository context provided.

If the answer is not present in the context, reply:

"I could not find enough information in the repository."

Never hallucinate.

Provide concise and technically accurate answers.
"""

    def build(
        self,
        question: str,
        contexts: List[str],
    ) -> str:
        """
        Build complete prompt.
        """

        prompt = self.SYSTEM_PROMPT.strip()

        prompt += "\n\n"

        prompt += "==============================\n"
        prompt += "Repository Context\n"
        prompt += "==============================\n\n"

        for index, context in enumerate(
            contexts,
            start=1,
        ):

            prompt += (
                f"[Context {index}]\n"
            )

            prompt += context.strip()

            prompt += "\n\n"

        prompt += "==============================\n"
        prompt += "User Question\n"
        prompt += "==============================\n\n"

        prompt += question

        prompt += "\n\n"

        prompt += "==============================\n"
        prompt += "Answer\n"
        prompt += "==============================\n"

        return prompt