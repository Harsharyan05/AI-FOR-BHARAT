"""
Prompt Builder V3 Test

Tests Prompt Builder V3 together with
Hybrid Retriever and the LLM.

Author: Harsh Aryan
Project: Cognisys
"""

from app.ai.prompt_builder_v3 import PromptBuilderV3
from app.ai.llm_engine import LLMEngine


def main():

    builder = PromptBuilderV3()

    llm = LLMEngine()

    history = []

    print("=" * 80)
    print("Prompt Builder V3")
    print("=" * 80)

    while True:

        question = input(
            "\nQuestion (type 'exit' to quit): "
        ).strip()

        if question.lower() == "exit":
            break

        # -------------------------------------------------
        # Build Prompt
        # -------------------------------------------------

        prompt = builder.build(
            question=question,
            history=history,
        )

        print("\nGenerated Prompt")
        print("=" * 80)
        print(prompt)

        # -------------------------------------------------
        # Send to LLM
        # -------------------------------------------------

        print("\nGenerating Response...")
        print("=" * 80)

        answer = llm.ask(
            prompt
        )

        print("\nAnswer")
        print("=" * 80)
        print(answer)

        # -------------------------------------------------
        # Save Conversation
        # -------------------------------------------------

        history.append(
            (
                question,
                answer,
            )
        )

        print("\n")
        print("=" * 80)
        print(
            f"Conversation Length : {len(history)}"
        )


if __name__ == "__main__":
    main()