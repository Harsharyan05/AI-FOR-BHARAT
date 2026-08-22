"""
Hybrid Retriever Test

Tests the hybrid retrieval engine using
semantic search + keyword search + document priority.

Author: Harsh Aryan
Project: Cognisys
"""

from app.ai.hybrid_retriever import HybridRetriever


def main():

    retriever = HybridRetriever()

    print("\nHybrid Repository Search")
    print("=" * 80)

    while True:

        question = input(
            "\nQuestion (type 'exit' to quit): "
        ).strip()

        if question.lower() == "exit":
            break

        results = retriever.retrieve(question)

        print("\nRetrieved Chunks")
        print("=" * 80)

        if not results:

            print("No matching chunks found.")
            continue

        for index, (
            score,
            embedding,
            distance,
        ) in enumerate(results, start=1):

            print(f"\nResult {index}")
            print("-" * 80)

            print(
                f"Document      : {embedding.source_document}"
            )

            print(
                f"Title         : {embedding.title}"
            )

            print(
                f"Chunk ID      : {embedding.chunk_id}"
            )

            print(
                f"Word Count    : {embedding.word_count}"
            )

            print(
                f"Embedding Dim : {embedding.dimension}"
            )

            print(
                f"Semantic Dist : {distance:.4f}"
            )

            print(
                f"Hybrid Score  : {score:.2f}"
            )

            preview = embedding.text[:250]

            if len(embedding.text) > 250:
                preview += "..."

            print("\nPreview")
            print("-" * 80)
            print(preview)

        print("\n")
        print("=" * 80)
        print(
            f"Retrieved {len(results)} ranked chunks."
        )


if __name__ == "__main__":
    main()