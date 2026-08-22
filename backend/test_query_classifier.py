"""
Test Query Classifier

Author: Harsh Aryan
Project: Cognisys
"""

from app.ai.query_classifier import (
    QueryClassifier,
)


def main():

    classifier = QueryClassifier()

    print("\nQuery Classifier")
    print("=" * 70)

    while True:

        question = input(
            "\nQuestion (exit to quit): "
        )

        if question.lower() == "exit":
            break

        result = classifier.classify(
            question
        )

        print("\nClassification")
        print("-" * 70)

        print(
            f"Category   : {result.category}"
        )

        print(
            f"Confidence : {result.confidence:.2f}"
        )

        print(
            f"Top-K      : {result.top_k}"
        )

        print(
            f"Overview   : {result.overview}"
        )

        print(
            f"Keywords   : {', '.join(result.keywords) if result.keywords else 'None'}"
        )


if __name__ == "__main__":
    main()