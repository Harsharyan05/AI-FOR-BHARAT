from app.ai.chunker import Chunker


def main():

    chunker = Chunker(
        "storage/documents/repository_summary.md"
    )

    chunks = chunker.chunk()

    print("\nGenerated Chunks")
    print("=" * 70)

    for chunk in chunks:

        print(
            f"\nChunk {chunk.id:03}"
        )

        print(
            f"Title      : {chunk.title}"
        )

        print(
            f"Words      : {chunk.word_count}"
        )

        print(
            f"Lines      : {chunk.line_count}"
        )

        print(
            f"Saved As   : chunk_{chunk.id:03}.md"
        )


if __name__ == "__main__":
    main()