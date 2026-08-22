"""
Recommendation Models

Author: Harsh Aryan
Project: Cognisys
"""

from dataclasses import dataclass


@dataclass
class Recommendation:

    priority: str
    title: str
    module: str
    recommendation: str