from app.ai.chunker import Chunker
from app.ai.embedding_generator import (
    EmbeddingGenerator,
)


def main():

    chunker = Chunker(
        "storage/documents/repository_summary.md"
    )

    chunks = chunker.chunk()

    generator = EmbeddingGenerator()

    embeddings = generator.generate(
        chunks
    )

    print("\nGenerated Embeddings")
    print("=" * 70)

    for embedding in embeddings:

        print(
            f"\nChunk ID     : {embedding.chunk_id}"
        )

        print(
            f"Title        : {embedding.title}"
        )

        print(
            f"Dimension    : {embedding.dimension}"
        )

        print(
            f"Word Count   : {embedding.word_count}"
        )

        print(
            f"Vector Size  : {len(embedding.vector)}"
        )


if __name__ == "__main__":
    main()