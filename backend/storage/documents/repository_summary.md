# Repository Summary

**Repository:** backend

**Generated On:** 01-08-2026 16:46:18

## Table of Contents

- Repository Statistics
- Repository Health
- Architecture Layers
- Repository Hotspots
- Architecture Patterns
- Circular Dependencies
- Recommendations

## Repository Statistics

- Modules: 77
- Architecture Layers: 6
- Hotspots: 63
- Patterns Detected: 3
- Circular Dependencies: 0
- Recommendations: 14

## Repository Health

- Overall Health: **GOOD**
- High Risk Modules: 0
- Circular Dependencies: 0
- Architecture Patterns: 3

## Architecture Layers

### Knowledge
- app\ai
- app\graph

### Presentation
- app\api

### Infrastructure
- app\architecture
- app\core
- app\security

### Persistence
- app\database
- app\models
- app\schemas

### Analysis
- app\parser

### Business
- app\services
- app\workflows

## Repository Hotspots

### HIGH Risk

None

### MEDIUM Risk

- **app.architecture.architecture_engine** | Fan-In: 0 | Fan-Out: 8 | Score: 8
- **app.graph.graph_models** | Fan-In: 5 | Fan-Out: 3 | Score: 8
- **app.architecture.report_generator** | Fan-In: 1 | Fan-Out: 6 | Score: 7
- **app.services.repository_service** | Fan-In: 2 | Fan-Out: 5 | Score: 7
- **app.main** | Fan-In: 0 | Fan-Out: 6 | Score: 6
- **app.architecture.architecture_models** | Fan-In: 3 | Fan-Out: 2 | Score: 5
- **app.architecture.hotspot_detector** | Fan-In: 3 | Fan-Out: 2 | Score: 5
- **app.architecture.recommendation_engine** | Fan-In: 1 | Fan-Out: 4 | Score: 5
- **app.parser.repository_cloner** | Fan-In: 1 | Fan-Out: 4 | Score: 5
- **app.services.analysis_service** | Fan-In: 1 | Fan-Out: 4 | Score: 5
- **app.services.knowledge_graph_service** | Fan-In: 0 | Fan-Out: 5 | Score: 5
- **app.api.v1.analysis** | Fan-In: 1 | Fan-Out: 4 | Score: 5

### LOW Risk

- **app.api.router** | Fan-In: 1 | Fan-Out: 3 | Score: 4
- **app.architecture.dependency_graph** | Fan-In: 1 | Fan-Out: 3 | Score: 4
- **app.core.logger** | Fan-In: 2 | Fan-Out: 2 | Score: 4
- **app.graph.entity_extractor** | Fan-In: 1 | Fan-Out: 3 | Score: 4
- **app.graph.graph_builder** | Fan-In: 1 | Fan-Out: 3 | Score: 4
- **app.parser.dependency_analyzer** | Fan-In: 2 | Fan-Out: 2 | Score: 4
- **app.parser.technology_detector** | Fan-In: 2 | Fan-Out: 2 | Score: 4
- **app.api.v1.repository** | Fan-In: 1 | Fan-Out: 3 | Score: 4
- **app.ai.document_generator** | Fan-In: 0 | Fan-Out: 3 | Score: 3
- **app.architecture.architecture_pattern_detector** | Fan-In: 1 | Fan-Out: 2 | Score: 3
- **app.architecture.layer_detector** | Fan-In: 1 | Fan-Out: 2 | Score: 3
- **app.architecture.recommendation_models** | Fan-In: 2 | Fan-Out: 1 | Score: 3
- **app.architecture.service_detector** | Fan-In: 0 | Fan-Out: 3 | Score: 3
- **app.core.config** | Fan-In: 2 | Fan-Out: 1 | Score: 3
- **app.core.constants** | Fan-In: 2 | Fan-Out: 1 | Score: 3
- **app.database.db** | Fan-In: 1 | Fan-Out: 2 | Score: 3
- **app.graph.relationship_extractor** | Fan-In: 1 | Fan-Out: 2 | Score: 3
- **app.parser.architecture_analyzer** | Fan-In: 2 | Fan-Out: 1 | Score: 3
- **app.parser.file_classifier** | Fan-In: 1 | Fan-Out: 2 | Score: 3
- **app.parser.import_graph_builder** | Fan-In: 1 | Fan-Out: 2 | Score: 3
- **app.parser.python_ast_parser** | Fan-In: 1 | Fan-Out: 2 | Score: 3
- **app.parser.repository_scanner** | Fan-In: 2 | Fan-Out: 1 | Score: 3
- **app.parser.symbol_extractor** | Fan-In: 1 | Fan-Out: 2 | Score: 3
- **app.schemas.analysis** | Fan-In: 1 | Fan-Out: 2 | Score: 3
- **app.schemas.repository** | Fan-In: 1 | Fan-Out: 2 | Score: 3
- **app.architecture.circular_dependency_detector** | Fan-In: 1 | Fan-Out: 1 | Score: 2
- **app.architecture.entry_point_detector** | Fan-In: 0 | Fan-Out: 2 | Score: 2
- **app.database.session** | Fan-In: 0 | Fan-Out: 2 | Score: 2
- **app.graph.graph_serializer** | Fan-In: 1 | Fan-Out: 1 | Score: 2
- **app.parser.call_graph_builder** | Fan-In: 0 | Fan-Out: 2 | Score: 2
- **app.models.repository_metadeta** | Fan-In: 0 | Fan-Out: 1 | Score: 1
- **app.ai.chat** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.ai.llm** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.ai.prompt_templates** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.ai.reasoning** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.database.models** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.graph.blast_radius** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.graph.graph_utils** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.security.dependency_checker** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.security.permission_checker** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.security.report_generator** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.security.secret_scanner** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.services.analyze_repository** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.services.generate_report** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.workflows.github_actions** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.workflows.trigger_parser** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.workflows.workflow_graph** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.api.v1.chat** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.api.v1.graph** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.api.v1.security** | Fan-In: 0 | Fan-Out: 0 | Score: 0
- **app.api.v1.workflow** | Fan-In: 0 | Fan-Out: 0 | Score: 0

## Architecture Patterns

### Layered Architecture
- Confidence: 0.95
- Evidence:
  - Business layer detected
  - Persistence layer detected
  - Presentation layer detected

### MVC
- Confidence: 0.60
- Evidence:
  - Presentation layer detected
  - Persistence layer detected

### Monolithic Architecture
- Confidence: 0.85
- Evidence:
  - 77 modules detected
  - Single deployable project

## Circular Dependencies

No circular dependencies detected.

## Recommendations

### Medium Coupling
- Priority: MEDIUM
- Module: app.architecture.architecture_engine
- Recommendation: Consider refactoring this module if it continues to grow.

### Medium Coupling
- Priority: MEDIUM
- Module: app.graph.graph_models
- Recommendation: Consider refactoring this module if it continues to grow.

### Medium Coupling
- Priority: MEDIUM
- Module: app.architecture.report_generator
- Recommendation: Consider refactoring this module if it continues to grow.

### Medium Coupling
- Priority: MEDIUM
- Module: app.services.repository_service
- Recommendation: Consider refactoring this module if it continues to grow.

### Medium Coupling
- Priority: MEDIUM
- Module: app.main
- Recommendation: Consider refactoring this module if it continues to grow.

### Medium Coupling
- Priority: MEDIUM
- Module: app.architecture.architecture_models
- Recommendation: Consider refactoring this module if it continues to grow.

### Medium Coupling
- Priority: MEDIUM
- Module: app.architecture.hotspot_detector
- Recommendation: Consider refactoring this module if it continues to grow.

### Medium Coupling
- Priority: MEDIUM
- Module: app.architecture.recommendation_engine
- Recommendation: Consider refactoring this module if it continues to grow.

### Medium Coupling
- Priority: MEDIUM
- Module: app.parser.repository_cloner
- Recommendation: Consider refactoring this module if it continues to grow.

### Medium Coupling
- Priority: MEDIUM
- Module: app.services.analysis_service
- Recommendation: Consider refactoring this module if it continues to grow.

### Medium Coupling
- Priority: MEDIUM
- Module: app.services.knowledge_graph_service
- Recommendation: Consider refactoring this module if it continues to grow.

### Medium Coupling
- Priority: MEDIUM
- Module: app.api.v1.analysis
- Recommendation: Consider refactoring this module if it continues to grow.

### Architecture Pattern
- Priority: LOW
- Module: Repository
- Recommendation: Layered architecture detected. Continue enforcing layer separation.

### Scalability
- Priority: LOW
- Module: Repository
- Recommendation: Consider modularization or microservices as the project grows.

