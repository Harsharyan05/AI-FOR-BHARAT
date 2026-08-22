"""
Knowledge Graph Builder

Author: Harsh Aryan
Project: Cognisys
"""

from app.graph.graph_models import KnowledgeGraph
from app.graph.entity_extractor import EntityExtractor
from app.graph.relationship_extractor import RelationshipExtractor


class GraphBuilder:
    """
    Builds a complete Knowledge Graph
    from a repository.
    """

    def __init__(self):

        self.entity_extractor = EntityExtractor()
        self.relationship_extractor = RelationshipExtractor()

    def build(self, repository_path: str):

        graph = KnowledgeGraph()

        nodes = self.entity_extractor.extract(
            repository_path
        )

        edges = self.relationship_extractor.extract(
            repository_path
        )

        for node in nodes:
            graph.add_node(node)

        for edge in edges:
            graph.add_edge(edge)

        return graph