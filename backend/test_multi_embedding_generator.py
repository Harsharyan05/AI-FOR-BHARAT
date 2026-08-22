from app.ai.multi_embedding_generator import (
    MultiEmbeddingGenerator,
)


def main():

    generator = MultiEmbeddingGenerator()

    embeddings = generator.generate()

    print("\nGenerated Embeddings")

    print("=" * 70)

    print()

    print(
        f"Total Embeddings : {len(embeddings)}\n"
    )

    for embedding in embeddings:

        print(
            f"Chunk {embedding.chunk_id:03}"
        )

        print(
            f"Document : {embedding.source_document}"
        )

        print(
            f"Title    : {embedding.title}"
        )

        print(
            f"Words    : {embedding.word_count}"
        )

        print(
            f"Dimension: {embedding.dimension}"
        )

        print("-" * 60)


if __name__ == "__main__":
    main()