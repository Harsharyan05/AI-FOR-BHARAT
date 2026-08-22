"""
Conversation Memory

Maintains conversational context for Cognisys by
storing previous user questions and AI responses.

Author: Harsh Aryan
Project: Cognisys
"""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class ConversationTurn:
    """
    Represents a single conversation turn.
    """

    question: str
    answer: str


class ConversationMemory:
    """
    Stores conversation history.

    Features
    --------
    • Add conversations
    • Retrieve complete history
    • Retrieve recent history
    • Limit memory size
    • Clear memory
    • Format history for PromptBuilderV3
    • Display stored conversations
    """

    def __init__(
        self,
        max_history: int = 10,
    ) -> None:
        """
        Initialize conversation memory.
        """

        self.max_history = max_history
        self.history: List[ConversationTurn] = []

    # ---------------------------------------------------------
    # Add Conversation
    # ---------------------------------------------------------

    def add(
        self,
        question: str,
        answer: str,
    ) -> None:
        """
        Adds a new conversation turn.
        """

        self.history.append(
            ConversationTurn(
                question=question,
                answer=answer,
            )
        )

        if len(self.history) > self.max_history:
            self.history.pop(0)

    # ---------------------------------------------------------
    # Get Complete History
    # ---------------------------------------------------------

    def get_history(
        self,
    ) -> List[Tuple[str, str]]:
        """
        Returns the complete conversation history.
        """

        return [
            (
                turn.question,
                turn.answer,
            )
            for turn in self.history
        ]

    # ---------------------------------------------------------
    # Get Recent History
    # ---------------------------------------------------------

    def get_recent(
        self,
        count: int = 5,
    ) -> List[Tuple[str, str]]:
        """
        Returns the most recent conversation turns.
        """

        return [
            (
                turn.question,
                turn.answer,
            )
            for turn in self.history[-count:]
        ]

    # ---------------------------------------------------------
    # Format for Prompt Builder
    # ---------------------------------------------------------

    def formatted_history(
        self,
        count: int = 5,
    ) -> List[Tuple[str, str]]:
        """
        Returns history formatted for PromptBuilderV3.
        """

        return self.get_recent(count)

    # ---------------------------------------------------------
    # Conversation Count
    # ---------------------------------------------------------

    def size(
        self,
    ) -> int:
        """
        Returns the number of stored conversations.
        """

        return len(self.history)

    # ---------------------------------------------------------
    # Check Empty
    # ---------------------------------------------------------

    def is_empty(
        self,
    ) -> bool:
        """
        Returns True if memory is empty.
        """

        return len(self.history) == 0

    # ---------------------------------------------------------
    # Get Last Conversation
    # ---------------------------------------------------------

    def last(
        self,
    ) -> Tuple[str, str] | None:
        """
        Returns the most recent conversation.
        """

        if self.is_empty():
            return None

        last_turn = self.history[-1]

        return (
            last_turn.question,
            last_turn.answer,
        )

    # ---------------------------------------------------------
    # Remove Last Conversation
    # ---------------------------------------------------------

    def remove_last(
        self,
    ) -> None:
        """
        Removes the latest conversation.
        """

        if not self.is_empty():
            self.history.pop()

    # ---------------------------------------------------------
    # Clear Memory
    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clears the conversation memory.
        """

        self.history.clear()

    # ---------------------------------------------------------
    # Display Memory
    # ---------------------------------------------------------

    def display(
        self,
    ) -> None:
        """
        Prints all stored conversations.
        """

        print("\n")
        print("=" * 80)
        print("Conversation Memory")
        print("=" * 80)

        if self.is_empty():

            print("Memory is empty.")
            print("=" * 80)
            return

        for index, turn in enumerate(
            self.history,
            start=1,
        ):

            print(f"\nConversation {index}")
            print("-" * 80)

            print("User")
            print(turn.question)

            print("\nAssistant")
            print(turn.answer)

        print("\n")
        print("=" * 80)

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def statistics(
        self,
    ) -> None:
        """
        Displays memory statistics.
        """

        print("\n")
        print("=" * 60)
        print("Conversation Memory Statistics")
        print("=" * 60)

        print(
            f"Stored Conversations : {self.size()}"
        )

        print(
            f"Maximum History      : {self.max_history}"
        )

        if self.is_empty():

            print("Latest Question      : None")

        else:

            print(
                f"Latest Question      : {self.history[-1].question}"
            )

        print("=" * 60)