"""
Repository service.

Author: Harsh Aryan
Project: Cognisys
"""

from app.parser.repository_cloner import RepositoryCloner
from app.parser.repository_scanner import RepositoryScanner
from app.parser.technology_detector import TechnologyDetector
from app.parser.dependency_analyzer import DependencyAnalyzer
from app.parser.architecture_analyzer import ArchitectureAnalyzer

class RepositoryService:

    @staticmethod
    def clone_repository(repository_url: str) -> dict:

        repository_name, local_path = RepositoryCloner.clone(
            repository_url
        )

        return {
            "status": "success",
            "repository_name": repository_name,
            "local_path": local_path,
        }

    @staticmethod
    def scan_repository(repository_path: str) -> dict:

        scanner = RepositoryScanner()

        return scanner.scan(repository_path)
    
    @staticmethod
    def detect_technology(repository_path: str):

        detector = TechnologyDetector()

        return detector.detect(repository_path)
    @staticmethod
    def analyze_dependencies(repository_path: str):

        analyzer = DependencyAnalyzer()

        return analyzer.analyze(repository_path)
    
    @staticmethod
    def analyze_architecture(repository_path: str):

        analyzer = ArchitectureAnalyzer()

        return analyzer.analyze(repository_path)