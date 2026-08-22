# Dependency Graph

This document contains the module dependency graph generated from the repository.

## Summary

- Total Modules : 85
- Total Dependencies : 140

---

## app.__init__

Dependency Count : 0

No imported modules.

---

## app.ai.__init__

Dependency Count : 0

No imported modules.

---

## app.ai.chat

Dependency Count : 0

No imported modules.

---

## app.ai.chunk_models

Dependency Count : 1

### Imports

- dataclasses

---

## app.ai.chunker

Dependency Count : 3

### Imports

- app.ai.chunk_models
- pathlib
- typing

---

## app.ai.document_generator

Dependency Count : 3

### Imports

- datetime
- pathlib
- typing

---

## app.ai.embedding_generator

Dependency Count : 6

### Imports

- app.ai.chunk_models
- app.ai.embedding_models
- json
- pathlib
- sentence_transformers
- typing

---

## app.ai.embedding_models

Dependency Count : 2

### Imports

- dataclasses
- typing

---

## app.ai.knowledge_document_generator

Dependency Count : 5

### Imports

- app.architecture.dependency_graph
- app.architecture.service_detector
- app.parser.technology_detector
- pathlib
- typing

---

## app.ai.llm

Dependency Count : 0

No imported modules.

---

## app.ai.prompt_builder

Dependency Count : 1

### Imports

- typing

---

## app.ai.prompt_templates

Dependency Count : 0

No imported modules.

---

## app.ai.reasoning

Dependency Count : 0

No imported modules.

---

## app.ai.semantic_search

Dependency Count : 3

### Imports

- app.ai.vector_store
- sentence_transformers
- typing

---

## app.ai.vector_store

Dependency Count : 5

### Imports

- faiss
- json
- numpy
- pathlib
- typing

---

## app.api.__init__

Dependency Count : 0

No imported modules.

---

## app.api.router

Dependency Count : 3

### Imports

- app.api.v1.analysis
- app.api.v1.repository
- fastapi

---

## app.api.v1.__init__

Dependency Count : 0

No imported modules.

---

## app.api.v1.analysis

Dependency Count : 4

### Imports

- app.schemas.analysis
- app.services.analysis_service
- app.services.repository_service
- fastapi

---

## app.api.v1.chat

Dependency Count : 0

No imported modules.

---

## app.api.v1.graph

Dependency Count : 0

No imported modules.

---

## app.api.v1.repository

Dependency Count : 3

### Imports

- app.schemas.repository
- app.services.repository_service
- fastapi

---

## app.api.v1.security

Dependency Count : 0

No imported modules.

---

## app.api.v1.workflow

Dependency Count : 0

No imported modules.

---

## app.architecture.architecture_engine

Dependency Count : 8

### Imports

- app.architecture.architecture_pattern_detector
- app.architecture.circular_dependency_detector
- app.architecture.dependency_graph
- app.architecture.hotspot_detector
- app.architecture.layer_detector
- app.architecture.recommendation_engine
- app.architecture.report_generator
- pathlib

---

## app.architecture.architecture_models

Dependency Count : 2

### Imports

- dataclasses
- typing

---

## app.architecture.architecture_pattern_detector

Dependency Count : 2

### Imports

- app.architecture.architecture_models
- typing

---

## app.architecture.circular_dependency_detector

Dependency Count : 1

### Imports

- typing

---

## app.architecture.dependency_graph

Dependency Count : 3

### Imports

- ast
- pathlib
- typing

---

## app.architecture.entry_point_detector

Dependency Count : 2

### Imports

- pathlib
- typing

---

## app.architecture.hotspot_detector

Dependency Count : 2

### Imports

- dataclasses
- typing

---

## app.architecture.layer_detector

Dependency Count : 2

### Imports

- pathlib
- typing

---

## app.architecture.recommendation_engine

Dependency Count : 4

### Imports

- app.architecture.architecture_models
- app.architecture.hotspot_detector
- app.architecture.recommendation_models
- typing

---

## app.architecture.recommendation_models

Dependency Count : 1

### Imports

- dataclasses

---

## app.architecture.report_generator

Dependency Count : 6

### Imports

- app.architecture.architecture_models
- app.architecture.hotspot_detector
- app.architecture.recommendation_models
- dataclasses
- json
- pathlib

---

## app.architecture.service_detector

Dependency Count : 3

### Imports

- ast
- pathlib
- typing

---

## app.core.__init__

Dependency Count : 0

No imported modules.

---

## app.core.config

Dependency Count : 1

### Imports

- pydantic_settings

---

## app.core.constants

Dependency Count : 1

### Imports

- pathlib

---

## app.core.logger

Dependency Count : 2

### Imports

- logging
- sys

---

## app.database.__init__

Dependency Count : 0

No imported modules.

---

## app.database.db

Dependency Count : 2

### Imports

- app.core.config
- sqlalchemy

---

## app.database.models

Dependency Count : 0

No imported modules.

---

## app.database.session

Dependency Count : 2

### Imports

- app.database.db
- sqlalchemy.orm

---

## app.graph.__init__

Dependency Count : 0

No imported modules.

---

## app.graph.blast_radius

Dependency Count : 0

No imported modules.

---

## app.graph.entity_extractor

Dependency Count : 3

### Imports

- app.graph.graph_models
- app.parser.file_classifier
- pathlib

---

## app.graph.graph_builder

Dependency Count : 3

### Imports

- app.graph.entity_extractor
- app.graph.graph_models
- app.graph.relationship_extractor

---

## app.graph.graph_models

Dependency Count : 3

### Imports

- dataclasses
- enum
- typing

---

## app.graph.graph_serializer

Dependency Count : 1

### Imports

- app.graph.graph_models

---

## app.graph.graph_utils

Dependency Count : 0

No imported modules.

---

## app.graph.relationship_extractor

Dependency Count : 2

### Imports

- app.graph.graph_models
- pathlib

---

## app.main

Dependency Count : 6

### Imports

- app.api.router
- app.core.config
- app.core.constants
- app.core.logger
- fastapi
- fastapi.middleware.cors

---

## app.models.__init__

Dependency Count : 0

No imported modules.

---

## app.models.repository_metadeta

Dependency Count : 1

### Imports

- dataclasses

---

## app.parser.__init__

Dependency Count : 0

No imported modules.

---

## app.parser.architecture_analyzer

Dependency Count : 1

### Imports

- pathlib

---

## app.parser.call_graph_builder

Dependency Count : 2

### Imports

- ast
- pathlib

---

## app.parser.dependency_analyzer

Dependency Count : 2

### Imports

- ast
- pathlib

---

## app.parser.file_classifier

Dependency Count : 2

### Imports

- app.graph.graph_models
- pathlib

---

## app.parser.import_graph_builder

Dependency Count : 2

### Imports

- ast
- pathlib

---

## app.parser.python_ast_parser

Dependency Count : 2

### Imports

- ast
- pathlib

---

## app.parser.repository_cloner

Dependency Count : 4

### Imports

- app.core.constants
- app.core.logger
- git
- pathlib

---

## app.parser.repository_scanner

Dependency Count : 1

### Imports

- pathlib

---

## app.parser.symbol_extractor

Dependency Count : 2

### Imports

- ast
- pathlib

---

## app.parser.technology_detector

Dependency Count : 2

### Imports

- json
- pathlib

---

## app.schemas.__init__

Dependency Count : 0

No imported modules.

---

## app.schemas.analysis

Dependency Count : 2

### Imports

- pydantic
- typing

---

## app.schemas.repository

Dependency Count : 2

### Imports

- pydantic
- typing

---

## app.security.__init__

Dependency Count : 0

No imported modules.

---

## app.security.dependency_checker

Dependency Count : 0

No imported modules.

---

## app.security.permission_checker

Dependency Count : 0

No imported modules.

---

## app.security.report_generator

Dependency Count : 0

No imported modules.

---

## app.security.secret_scanner

Dependency Count : 0

No imported modules.

---

## app.services.__init__

Dependency Count : 0

No imported modules.

---

## app.services.analysis_service

Dependency Count : 4

### Imports

- app.parser.architecture_analyzer
- app.parser.dependency_analyzer
- app.parser.repository_scanner
- app.parser.technology_detector

---

## app.services.analyze_repository

Dependency Count : 0

No imported modules.

---

## app.services.generate_report

Dependency Count : 0

No imported modules.

---

## app.services.knowledge_graph_service

Dependency Count : 5

### Imports

- app.graph.graph_builder
- app.graph.graph_serializer
- app.parser.import_graph_builder
- app.parser.python_ast_parser
- app.parser.symbol_extractor

---

## app.services.repository_service

Dependency Count : 5

### Imports

- app.parser.architecture_analyzer
- app.parser.dependency_analyzer
- app.parser.repository_cloner
- app.parser.repository_scanner
- app.parser.technology_detector

---

## app.utils.__init__

Dependency Count : 0

No imported modules.

---

## app.workflows.__init__

Dependency Count : 0

No imported modules.

---

## app.workflows.github_actions

Dependency Count : 0

No imported modules.

---

## app.workflows.trigger_parser

Dependency Count : 0

No imported modules.

---

## app.workflows.workflow_graph

Dependency Count : 0

No imported modules.

---

