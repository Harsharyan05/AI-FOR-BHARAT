"""
Knowledge Graph Service

Author: Harsh Aryan
Project: Cognisys
"""

from app.graph.graph_builder import GraphBuilder
from app.graph.graph_serializer import GraphSerializer

from app.parser.python_ast_parser import PythonASTParser
from app.parser.symbol_extractor import SymbolExtractor
from app.parser.import_graph_builder import ImportGraphBuilder


class KnowledgeGraphService:
    """
    Central service responsible for building
    the Software Knowledge Graph.
    """

    @staticmethod
    def build(repository_path: str):

        graph = GraphBuilder().build(repository_path)

        ast_data = PythonASTParser().parse(repository_path)

        symbols = SymbolExtractor().extract(repository_path)

        imports = ImportGraphBuilder().build(repository_path)

        return {

            "graph": GraphSerializer.serialize(graph),

            "ast": ast_data,

            "symbols": symbols,

            "imports": imports,

        }