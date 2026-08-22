"""
Knowledge Graph Serializer

Author: Harsh Aryan
Project: Cognisys
"""

from app.graph.graph_models import KnowledgeGraph


class GraphSerializer:
    """
    Converts a Knowledge Graph
    into JSON-serializable data.
    """

    @staticmethod
    def serialize(graph: KnowledgeGraph):

        return {

            "nodes": [

                {
                    "id": node.id,
                    "label": node.label,
                    "type": node.type,
                    "properties": node.properties,
                }

                for node in graph.nodes

            ],

            "edges": [

                {
                    "source": edge.source,
                    "target": edge.target,
                    "relationship": edge.relationship,
                    "properties": edge.properties,
                }

                for edge in graph.edges

            ],
        }