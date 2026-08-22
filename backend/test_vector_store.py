from app.ai.embedding_generator import (
    EmbeddingGenerator,
)

from app.ai.chunker import Chunker

from app.ai.vector_store import (
    VectorStore,
)


def main():

    chunker = Chunker(
        "storage/documents/repository_summary.md"
    )

    chunks = chunker.chunk()

    embeddings = EmbeddingGenerator().generate(
        chunks
    )

    store = VectorStore()

    store.build()

    print("\nVector Database Built")
    print("=" * 60)

    print(
        f"Vectors Indexed : {len(embeddings)}"
    )

    store.load()

    print("\nPerforming Sample Search\n")

    results = store.search(
        embeddings[0].vector,
        top_k=3,
    )

    for result in results:

        print(
            f"Chunk {result['chunk_id']}"
        )

        print(
            f"Title : {result['title']}"
        )

        print(
            f"Distance : {result['distance']:.4f}"
        )

        print("-" * 40)


if __name__ == "__main__":
    main()