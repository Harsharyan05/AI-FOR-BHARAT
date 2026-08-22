from app.ai.multi_document_chunker import (
    MultiDocumentChunker,
)


def main():

    chunker = MultiDocumentChunker()

    chunks = chunker.chunk()

    print("\nGenerated Semantic Chunks")
    print("=" * 80)

    print(
        f"\nTotal Chunks : {len(chunks)}\n"
    )

    for chunk in chunks:

        print(
            f"Chunk {chunk.chunk_id:03}"
        )

        print(
            f"Document : {chunk.source_document}"
        )

        print(
            f"Title    : {chunk.title}"
        )

        print(
            f"Words    : {chunk.word_count}"
        )

        print("-" * 60)


if __name__ == "__main__":
    main()