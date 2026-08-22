from app.parser.repository_scanner import RepositoryScanner
from app.parser.technology_detector import TechnologyDetector
from app.parser.dependency_analyzer import DependencyAnalyzer
from app.parser.architecture_analyzer import ArchitectureAnalyzer


class AnalysisService:

    @staticmethod
    def analyze(repository_path: str):

        scanner = RepositoryScanner()
        detector = TechnologyDetector()
        dependency = DependencyAnalyzer()
        architecture = ArchitectureAnalyzer()

        return {
            "repository": scanner.scan(repository_path),
            "technology": detector.detect(repository_path),
            "dependencies": dependency.analyze(repository_path),
            "architecture": architecture.analyze(repository_path),
        }