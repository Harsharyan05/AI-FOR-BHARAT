# Sprint 05 — Software Knowledge Graph Engine

**Project:** Cognisys – AI System Behaviour & Automation Intelligence Engine

**Sprint Duration:** Week 5

**Status:** ✅ Completed

---

# Sprint Objective

The objective of Sprint 5 was to transform Cognisys from a repository analysis platform into a **Software Knowledge Graph Engine** capable of understanding software structure, source code, dependencies, symbols, and execution relationships.

Unlike traditional repository analyzers that stop at file structures, Sprint 5 introduced semantic analysis using Python's AST and graph-based modeling.

---

# Architecture

```
GitHub Repository
        │
        ▼
Repository Cloner
        │
        ▼
Repository Scanner
        │
        ▼
Technology Detector
        │
        ▼
Dependency Analyzer
        │
        ▼
Architecture Analyzer
        │
        ▼
Python AST Parser
        │
        ▼
Symbol Extractor
        │
        ▼
Import Graph Builder
        │
        ▼
Call Graph Builder
        │
        ▼
Knowledge Graph
        │
        ▼
Knowledge Graph Service
```

---

# Features Implemented

## 1. Knowledge Graph Models

Implemented strongly typed graph models including:

- Node
- Edge
- KnowledgeGraph
- NodeType
- RelationshipType

These models provide the foundation for representing software systems as graph structures.

---

## 2. Entity Extractor

Developed an entity extraction engine that converts repository contents into graph nodes.

Detected entities include:

- Repository
- Folder
- Python File
- Documentation
- Configuration
- Service
- API
- Workflow
- Technology

---

## 3. Relationship Extractor

Implemented graph relationship discovery.

Current supported relationships:

- contains

Future relationships such as `calls`, `uses`, `inherits`, and `implements` will extend this graph.

---

## 4. Graph Builder

Implemented a centralized graph construction engine responsible for combining extracted entities and relationships into a unified Software Knowledge Graph.

---

## 5. Graph Serializer

Implemented JSON serialization for graph export.

This enables future integration with:

- React Flow
- Cytoscape
- D3.js
- Neo4j
- AI Reasoning Engine

---

## 6. Python AST Parser

Implemented Python Abstract Syntax Tree parsing using Python's built-in `ast` module.

Extracted information includes:

- Imports
- Classes
- Functions
- Async Functions

This enables Cognisys to understand source code beyond plain text analysis.

---

## 7. Symbol Extractor

Implemented symbol extraction for Python source files.

Extracted symbols:

- Classes
- Functions

These symbols become semantic entities inside the Software Knowledge Graph.

---

## 8. Intelligent File Classifier

Developed a rule-based classifier that categorizes repository files according to their software role.

Current classifications include:

- Python File
- Service
- API Endpoint
- Documentation
- Configuration
- Workflow
- Technology

---

## 9. Import Graph Builder

Implemented import dependency extraction using Python AST.

This enables Cognisys to understand module dependencies across the project.

Example:

```
analysis.py
      │
 imports
      ▼
analysis_service.py
```

---

## 10. Call Graph Builder

Implemented function-level call graph generation.

Current capabilities:

- Function call discovery
- Method invocation tracking
- Internal execution flow analysis

Example:

```
analyze_repository()

        │

      calls

        ▼

AnalysisService.analyze()

        │

      calls

        ▼

RepositoryScanner.scan()
```

---

## 11. Knowledge Graph Service

Implemented a unified service responsible for aggregating all repository intelligence into a single interface.

Collected information includes:

- Repository Graph
- AST Analysis
- Symbols
- Import Graph
- Call Graph

This service becomes the central backend component consumed by future AI and visualization modules.

---

# Testing

The following testing utilities were created and executed successfully.

- test_graph.py
- test_serializer.py
- test_entities.py
- test_relationships.py
- test_ast.py
- test_symbols.py
- test_imports.py
- test_classifier.py
- test_call_graph.py
- test_knowledge_graph.py

---

# Technical Highlights

- Python AST-based static analysis
- Knowledge Graph architecture
- Graph serialization
- Function call extraction
- Import dependency graph
- Semantic symbol extraction
- Repository intelligence pipeline

---

# Sprint Deliverables

- Software Knowledge Graph
- Repository Intelligence Engine
- AST Parsing Engine
- Import Dependency Analysis
- Function Call Graph
- Unified Knowledge Graph Service

---

# Challenges Solved

During Sprint 5 several engineering issues were identified and resolved:

- Repository cloning permission conflicts
- Windows file locking during repository cleanup
- FastAPI router integration
- Schema import resolution
- Graph model redesign
- Entity extraction improvements
- Intelligent file classification
- Call graph implementation

---

# Outcome

Sprint 5 successfully established the core Software Knowledge Graph infrastructure required for higher-level reasoning.

Cognisys can now:

- Understand repository structure
- Analyze source code
- Extract semantic symbols
- Build dependency graphs
- Build function call graphs
- Represent software systems as knowledge graphs

This sprint transforms Cognisys from a repository analyzer into a platform capable of supporting software architecture intelligence.

---

# Next Sprint

## Sprint 06 — Software Architecture Intelligence

Upcoming features include:

- Entry Point Detection
- Layer Detection
- Service Discovery
- Circular Dependency Detection
- Hotspot Analysis
- Architecture Pattern Recognition
- Architecture Report Generation

These modules will leverage the Software Knowledge Graph developed during Sprint 5 to generate architectural insights.
