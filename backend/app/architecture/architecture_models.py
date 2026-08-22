"""
Architecture Models

Author: Harsh Aryan
Project: Cognisys
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class ArchitecturePattern:
    """
    Represents a detected architecture pattern.
    """

    name: str
    confidence: float
    evidence: List[str] = field(default_factory=list)