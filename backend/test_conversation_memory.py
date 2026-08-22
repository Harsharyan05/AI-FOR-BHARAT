"""
Conversation Memory Test

Author: Harsh Aryan
Project: Cognisys
"""

from app.ai.conversation_memory import (
    ConversationMemory,
)


def main():

    memory = ConversationMemory(
        max_history=5,
    )

    while True:

        question = input(
            "\nQuestion (exit to quit): "
        ).strip()

        if question.lower() == "exit":
            break

        answer = input(
            "Answer: "
        ).strip()

        memory.add(
            question,
            answer,
        )

        print("\nStored Successfully!")

        print(
            f"Memory Size : {memory.size()}"
        )

        print("\nRecent History")

        for q, a in memory.get_recent():

            print("-" * 60)

            print(f"Q : {q}")

            print(f"A : {a}")

    print("\n")

    memory.display()


if __name__ == "__main__":
    main()