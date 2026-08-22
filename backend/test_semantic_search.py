from app.ai.semantic_search import SemanticSearch


def main():

    search_engine = SemanticSearch()

    print("\nSemantic Repository Search")
    print("=" * 70)

    while True:

        query = input(
            "\nAsk about the repository (type 'exit' to quit): "
        )

        if query.lower() == "exit":
            break

        results = search_engine.search(
            query,
            top_k=5,
        )

        print("\nTop Matches")
        print("-" * 70)

        if not results:

            print("No relevant results found.")
            continue

        for result in results:

            print(
                f"\nChunk ID   : {result['chunk_id']}"
            )

            print(
                f"Title      : {result['title']}"
            )

            print(
                f"Distance   : {result['distance']:.4f}"
            )

            print(
                f"Words      : {result['word_count']}"
            )

            print("-" * 70)


if __name__ == "__main__":
    main()