"""
Test Multi Semantic Search

Author: Harsh Aryan
Project: Cognisys
"""

from app.ai.multi_embedding_generator import (
    MultiEmbeddingGenerator,
)

from app.ai.multi_vector_store import (
    MultiVectorStore,
)

from app.ai.multi_semantic_search import (
    MultiSemanticSearch,
)


def build_vector_database():

    generator = MultiEmbeddingGenerator()

    embeddings = generator.generate()

    store = MultiVectorStore()

    store.build(embeddings)


def main():

    build_vector_database()

    search = MultiSemanticSearch()

    print("\nSemantic Repository Search")

    print("=" * 70)

    while True:

        query = input(
            "\nAsk about the repository (type 'exit' to quit): "
        )

        if query.lower() == "exit":
            break

        results = search.search(
            query=query,
            top_k=5,
        )

        print("\nTop Results")

        print("=" * 70)

        if not results:

            print("No relevant chunks found.")

            continue

        for embedding, distance in results:

            print(f"\nChunk : {embedding.chunk_id}")

            print(
                f"Document : {embedding.source_document}"
            )

            print(
                f"Title : {embedding.title}"
            )

            print(
                f"Distance : {distance:.4f}"
            )

            print("\nPreview")

            preview = (
                embedding.text[:300]
                .replace("\n", " ")
            )

            print(preview)

            print("-" * 70)


if __name__ == "__main__":
    main()