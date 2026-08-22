"""
Test LLM Engine

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

from app.ai.prompt_builder_v2 import (
    PromptBuilderV2,
)

from app.ai.llm_engine import (
    LLMEngine,
)


def build_database():

    generator = MultiEmbeddingGenerator()

    embeddings = generator.generate()

    store = MultiVectorStore()

    store.build(
        embeddings
    )


def main():

    build_database()

    search = MultiSemanticSearch()

    builder = PromptBuilderV2()

    llm = LLMEngine()

    print("\nRepository AI Chat")
    print("=" * 70)

    while True:

        question = input(
            "\nQuestion (exit to quit): "
        )

        if question.lower() == "exit":
            break

        results = search.search(
            question,
            top_k=10,
        )

        prompt = builder.build(
            question=question,
            search_results=results,
        )

        answer = llm.ask(
            prompt
        )

        print("\nAnswer")
        print("=" * 70)
        print(answer)


if __name__ == "__main__":
    main()