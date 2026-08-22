"""
Hybrid Retriever

Combines semantic search with keyword scoring,
document priority, duplicate removal, and re-ranking
for improved repository knowledge retrieval.

Author: Harsh Aryan
Project: Cognisys
"""

import re
from typing import List, Tuple

from app.ai.multi_semantic_search import MultiSemanticSearch
from app.ai.query_classifier import QueryClassifier
from app.ai.embedding_models import Embedding


class HybridRetriever:
    """
    Hybrid Retrieval Engine.

    Combines:
    - Semantic Search
    - Keyword Matching
    - Document Priority
    - Hybrid Scoring
    - Duplicate Removal
    - Re-ranking
    - Adaptive Top-K Retrieval
    """

    # ---------------------------------------------------------
    # Document Priority
    # ---------------------------------------------------------

    DOCUMENT_PRIORITY = {
        "repository_summary.md": 10,
        "architecture.md": 9,
        "services.md": 8,
        "apis.md": 8,
        "dependency_graph.md": 7,
        "technologies.md": 7,
        "architecture_patterns.md": 6,
        "hotspots.md": 5,
        "recommendations.md": 4,
    }

    # ---------------------------------------------------------
    # Stop Words
    # ---------------------------------------------------------

    STOP_WORDS = {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "by",
        "for",
        "from",
        "how",
        "in",
        "is",
        "it",
        "of",
        "on",
        "or",
        "that",
        "the",
        "this",
        "to",
        "what",
        "where",
        "which",
        "who",
        "with",
    }

    # ---------------------------------------------------------
    # Initialization
    # ---------------------------------------------------------

    def __init__(self):

        self.semantic_search = MultiSemanticSearch()

        self.classifier = QueryClassifier()

        self.document_priority = (
            self.DOCUMENT_PRIORITY.copy()
        )

    # ---------------------------------------------------------
    # Query Tokenization
    # ---------------------------------------------------------

    def _extract_keywords(
        self,
        query: str,
    ) -> List[str]:
        """
        Extract meaningful keywords from a user query.
        """

        words = re.findall(
            r"[a-zA-Z0-9_\-\.]+",
            query.lower(),
        )

        keywords = [
            word
            for word in words
            if word not in self.STOP_WORDS
            and len(word) > 1
        ]

        return keywords

    # ---------------------------------------------------------
    # Keyword Search
    # ---------------------------------------------------------

    def keyword_search(
        self,
        query: str,
        semantic_results,
    ):
        """
        Calculate keyword relevance for semantic results.
        """

        words = self._extract_keywords(
            query
        )

        results = []

        for embedding, distance in semantic_results:

            keyword_score = 0

            title = (
                embedding.title or ""
            ).lower()

            source_document = (
                embedding.source_document or ""
            ).lower()

            content = (
                embedding.text or ""
            ).lower()

            # ---------------------------------------------
            # Keyword scoring
            # ---------------------------------------------

            for word in words:

                # Title matches are highly important.
                if word in title:
                    keyword_score += 3

                # Document-name matches are important.
                if word in source_document:
                    keyword_score += 2

                # Content matches.
                if word in content:
                    keyword_score += 1

            results.append(
                (
                    embedding,
                    distance,
                    keyword_score,
                )
            )

        return results

    # ---------------------------------------------------------
    # Semantic Score
    # ---------------------------------------------------------

    @staticmethod
    def _semantic_score(
        distance: float,
    ) -> float:
        """
        Convert FAISS L2 distance into a relevance score.

        Lower distance = higher relevance.
        """

        if distance < 0:
            distance = 0

        return 1.0 / (
            1.0 + distance
        )

    # ---------------------------------------------------------
    # Document Priority
    # ---------------------------------------------------------

    def _document_priority(
        self,
        embedding: Embedding,
    ) -> int:
        """
        Return priority score for the source document.
        """

        source_document = (
            embedding.source_document or ""
        )

        # Handle paths such as:
        # storage/documents/architecture.md

        filename = (
            source_document
            .replace("\\", "/")
            .split("/")[-1]
        )

        return self.document_priority.get(
            filename,
            1,
        )

    # ---------------------------------------------------------
    # Final Hybrid Score
    # ---------------------------------------------------------

    def calculate_score(
        self,
        embedding: Embedding,
        distance: float,
        keyword_score: int,
    ) -> float:
        """
        Calculate final hybrid relevance score.
        """

        semantic_score = (
            self._semantic_score(
                distance
            )
        )

        priority = (
            self._document_priority(
                embedding
            )
        )

        # ---------------------------------------------
        # Weighted hybrid scoring
        # ---------------------------------------------

        final_score = (
            semantic_score * 10.0
            + keyword_score * 2.0
            + priority
        )

        return float(
            final_score
        )

    # ---------------------------------------------------------
    # Re-ranking
    # ---------------------------------------------------------

    def rerank(
        self,
        results,
    ):
        """
        Re-rank results using the hybrid score.
        """

        ranked = []

        for (
            embedding,
            distance,
            keyword_score,
        ) in results:

            score = self.calculate_score(
                embedding=embedding,
                distance=distance,
                keyword_score=keyword_score,
            )

            ranked.append(
                (
                    score,
                    embedding,
                    distance,
                )
            )

        ranked.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return ranked

    # ---------------------------------------------------------
    # Duplicate Removal
    # ---------------------------------------------------------

    def remove_duplicates(
        self,
        ranked_results,
    ):
        """
        Remove duplicate repository chunks.
        """

        unique = []

        seen = set()

        for (
            score,
            embedding,
            distance,
        ) in ranked_results:

            # IMPORTANT:
            # Embedding uses source_document,
            # not document.

            key = (
                embedding.source_document,
                embedding.chunk_id,
            )

            if key in seen:
                continue

            seen.add(
                key
            )

            unique.append(
                (
                    score,
                    embedding,
                    distance,
                )
            )

        return unique

    # ---------------------------------------------------------
    # Retrieval
    # ---------------------------------------------------------

    def retrieve(
        self,
        question: str,
        top_k: int | None = None,
    ):
        """
        Retrieve the most relevant repository chunks.

        Pipeline:

        Question
            ↓
        Query Classification
            ↓
        Semantic Retrieval
            ↓
        Keyword Scoring
            ↓
        Document Priority
            ↓
        Hybrid Re-ranking
            ↓
        Duplicate Removal
            ↓
        Top-K Results
        """

        if not question:
            return []

        question = question.strip()

        if not question:
            return []

        # ---------------------------------------------
        # Query Classification
        # ---------------------------------------------

        classification = (
            self.classifier.classify(
                question
            )
        )

        # ---------------------------------------------
        # Determine final Top-K
        # ---------------------------------------------

        final_top_k = (
            top_k
            if top_k is not None
            else classification.top_k
        )

        # ---------------------------------------------
        # Retrieve more candidates before reranking
        # ---------------------------------------------

        candidate_k = max(
            final_top_k * 2,
            15,
        )

        # ---------------------------------------------
        # Semantic Search
        # ---------------------------------------------

        semantic_results = (
            self.semantic_search.search(
                query=question,
                top_k=candidate_k,
            )
        )

        if not semantic_results:
            return []

        # ---------------------------------------------
        # Keyword Scoring
        # ---------------------------------------------

        keyword_results = (
            self.keyword_search(
                query=question,
                semantic_results=semantic_results,
            )
        )

        # ---------------------------------------------
        # Hybrid Re-ranking
        # ---------------------------------------------

        ranked_results = (
            self.rerank(
                keyword_results
            )
        )

        # ---------------------------------------------
        # Duplicate Removal
        # ---------------------------------------------

        unique_results = (
            self.remove_duplicates(
                ranked_results
            )
        )

        # ---------------------------------------------
        # Return Top Results
        # ---------------------------------------------

        return unique_results[
            :final_top_k
        ]