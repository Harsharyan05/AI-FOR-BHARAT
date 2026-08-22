"""
Prompt Builder V2

Builds high-quality prompts for repository question answering.

Author: Harsh Aryan
Project: Cognisys
"""

from typing import List, Tuple

from app.ai.embedding_models import Embedding


class PromptBuilderV2:
    """
    Builds prompts using retrieved repository context.
    """

    SYSTEM_PROMPT = """
You are Cognisys AI.

You are an expert Software Architect, Senior Backend Engineer,
DevOps Engineer, AI Engineer and Code Reviewer.

You answer ONLY using the repository context provided.

Rules:

1. Never hallucinate.
2. If the repository does not contain the answer, say:

"I could not find enough information in the repository."

3. Mention source documents whenever appropriate.
4. Keep answers technical and concise.
5. Prefer repository evidence over assumptions.
""".strip()

    def build(
        self,
        question: str,
        search_results: List[Tuple[Embedding, float]],
    ) -> str:
        """
        Build the final LLM prompt.
        """

        prompt = []

        prompt.append(self.SYSTEM_PROMPT)

        prompt.append("\n")
        prompt.append("=" * 70)
        prompt.append("\nRepository Context\n")
        prompt.append("=" * 70)
        prompt.append("\n")

        for index, (embedding, distance) in enumerate(
            search_results,
            start=1,
        ):

            prompt.append(
                f"[Context {index}]\n"
            )

            prompt.append(
                f"Source : {embedding.source_document}\n"
            )

            prompt.append(
                f"Title : {embedding.title}\n"
            )

            prompt.append(
                f"Similarity Distance : {distance:.4f}\n\n"
            )

            prompt.append(
                embedding.text.strip()
            )

            prompt.append("\n\n")

        prompt.append("=" * 70)
        prompt.append("\nUser Question\n")
        prompt.append("=" * 70)
        prompt.append("\n\n")

        prompt.append(question)

        prompt.append("\n\n")

        prompt.append("=" * 70)
        prompt.append("\nAnswer\n")
        prompt.append("=" * 70)
        prompt.append("\n")

        return "".join(prompt)