"""
Knowledge Graph Models

Author: Harsh Aryan
Project: Cognisys
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


# --------------------------------------------------
# Node Types
# --------------------------------------------------

class NodeType(str, Enum):

    REPOSITORY = "Repository"

    FOLDER = "Folder"

    PYTHON_FILE = "PythonFile"

    CLASS = "Class"

    FUNCTION = "Function"

    API_ENDPOINT = "APIEndpoint"

    SERVICE = "Service"

    DATABASE = "Database"

    TECHNOLOGY = "Technology"

    WORKFLOW = "Workflow"

    CONFIG = "Config"

    DOCUMENTATION = "Documentation"


# --------------------------------------------------
# Relationship Types
# --------------------------------------------------

class RelationshipType(str, Enum):

    CONTAINS = "contains"

    IMPORTS = "imports"

    DEFINES = "defines"

    CALLS = "calls"

    USES = "uses"

    DEPENDS_ON = "depends_on"

    INHERITS = "inherits"

    IMPLEMENTS = "implements"

    DECORATED_WITH = "decorated_with"


# --------------------------------------------------
# Node
# --------------------------------------------------

@dataclass
class Node:

    id: str

    label: str

    type: NodeType

    properties: dict[str, Any] = field(default_factory=dict)


# --------------------------------------------------
# Edge
# --------------------------------------------------

@dataclass
class Edge:

    source: str

    target: str

    relationship: RelationshipType

    properties: dict[str, Any] = field(default_factory=dict)


# --------------------------------------------------
# Graph
# --------------------------------------------------

@dataclass
class KnowledgeGraph:

    nodes: list[Node] = field(default_factory=list)

    edges: list[Edge] = field(default_factory=list)

    def add_node(self, node: Node):

        self.nodes.append(node)

    def add_edge(self, edge: Edge):

        self.edges.append(edge)