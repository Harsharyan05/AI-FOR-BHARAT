"""
Citation Engine Test

Tests the Citation Engine by retrieving
repository knowledge and generating citations.

Author: Harsh Aryan
Project: Cognisys
"""

from app.ai.hybrid_retriever import HybridRetriever
from app.ai.citation_engine import CitationEngine


def main():

    print("=" * 80)
    print("Citation Engine Test")
    print("=" * 80)

    retriever = HybridRetriever()

    citation_engine = CitationEngine()

    while True:

        question = input(
            "\nQuestion (type 'exit' to quit): "
        ).strip()

        if question.lower() == "exit":
            break

        print("\nRetrieving repository knowledge...")

        try:

            retrieved_results = retriever.retrieve(
                question
            )

        except Exception as error:

            print(f"\nRetrieval Error:\n{error}")
            continue

        if not retrieved_results:

            print("\nNo repository knowledge found.")
            continue

        citations = citation_engine.extract(
            retrieved_results
        )

        print("\n")
        print("=" * 80)
        print("Repository Citations")
        print("=" * 80)

        citation_engine.display(
            citations
        )

        print("\n")
        print("=" * 80)
        print("Markdown Output")
        print("=" * 80)

        print(
            citation_engine.to_markdown(
                citations
            )
        )

        print("\n")
        print("=" * 80)
        print(
            f"Generated {len(citations)} unique citations."
        )
        print("=" * 80)


if __name__ == "__main__":
    main()