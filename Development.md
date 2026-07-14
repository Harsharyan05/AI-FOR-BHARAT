# Cognisys Development Log

## Day 1 — Backend Foundation

### Objective

Establish a production-ready backend architecture for Cognisys using FastAPI.

# Completed

## Project Structure

Created a scalable backend folder structure.

---


# Day 2 — Repository Clone Engine

## Objective

Implement the first production-ready feature of Cognisys by enabling cloning of public GitHub repositories through a REST API.

---

## Completed

- Repository request schema
- Repository response schema
- Repository cloning engine
- Repository service layer
- API routing
- Swagger integration
- Error handling
- Logging

---

## API

POST /api/v1/repositories/clone

---

## Example

Input

{
    "repository_url":"https://github.com/user/project.git"
}

Output

{
    "status":"success",
    "repository_name":"project",
    "local_path":"storage/temp/project"
}

---

## Architecture

Client

↓

FastAPI

↓

Repository Service

↓

Repository Cloner

↓

GitPython

↓

Local Storage

Status

✅ Completed

---

## Day 3 — Repository Intelligence Engine

**Date:** 12 July 2026

---

# 🎯 Objective

Transform Cognisys from a repository cloning service into an intelligent repository analysis engine capable of understanding software projects through deterministic analysis.

---

# ✅ Features Completed

## 1. Repository Scanner

Implemented a repository scanning engine capable of extracting structural metadata.

### Extracted Information

- Repository name
- Total files
- Total directories
- File extensions
- Docker files
- Configuration files
- Documentation files
- GitHub workflow detection
- Largest files
- Empty directories

---

## 2. Technology Detection Engine

Developed a deterministic technology detection system without using LLMs.

### Supported Detection

### Languages

- Python
- JavaScript
- TypeScript

### Frameworks

- FastAPI
- React
- Next.js
- Tailwind CSS

### Databases

- PostgreSQL
- SQLAlchemy

### AI / ML Libraries

- LangChain
- NetworkX

### Deployment

- Docker

Technology detection is performed by analyzing configuration files such as:

- requirements.txt
- package.json
- pyproject.toml
- Dockerfile

---

## 3. Dependency Analyzer

Implemented dependency extraction using Python's Abstract Syntax Tree (AST).

### Features

- Detects Python imports
- Builds module dependency relationships
- Ignores comments and invalid syntax safely
- Generates dependency mappings for future graph construction

Example:

main.py

↓

RepositoryService

↓

RepositoryScanner

---

## 4. Architecture Analyzer

Implemented automatic architecture inference.

Current capabilities:

- Backend detection
- Frontend detection
- Full-stack detection
- Docker detection
- GitHub Actions detection
- Basic database detection

The analyzer produces a high-level architectural overview of the repository.

---

## 5. Analysis Service

Created a unified orchestration layer.

Pipeline:

Repository

↓

Scanner

↓

Technology Detector

↓

Dependency Analyzer

↓

Architecture Analyzer

↓

Combined Analysis Result

The Analysis Service acts as the central intelligence engine of Cognisys.

---

# 🏗 Architecture

```
GitHub Repository
        │
        ▼
Repository Clone Engine
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
Analysis Service
```

---

# 🧠 Engineering Decisions

During development several architectural improvements were introduced.

## Clean Architecture

Responsibilities are separated into independent modules.

- Parsers extract information.
- Services orchestrate business logic.
- APIs expose functionality.
- Schemas validate requests and responses.

---

## Deterministic Analysis

Rather than relying on Large Language Models for repository understanding, Cognisys first performs deterministic software analysis.

Benefits:

- Faster execution
- Higher accuracy
- Explainable results
- Lower operational cost

---

## Scalable Parser Design

Each parser focuses on a single concern.

Repository Scanner

↓

Technology Detector

↓

Dependency Analyzer

↓

Architecture Analyzer

This design enables future expansion without modifying existing components.

---

# 📂 Modules Added

```
parser/
├── repository_scanner.py
├── technology_detector.py
├── dependency_analyzer.py
└── architecture_analyzer.py

services/
├── repository_service.py
└── analysis_service.py
```

---

# 📈 Project Progress

Backend Foundation

██████████████████████████████ 100%

Repository Intelligence

████████████████████░░░░░░░░░ 70%

Frontend

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0%

AI Reasoning

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0%

Overall Project Progress

██████████████████░░░░░░░░░░░ 45%

---

# 🚀 Next Milestone

Sprint 4 — Unified Analysis API

Planned features:

- Repository analysis endpoint
- End-to-end analysis pipeline
- Structured JSON responses
- Frontend integration

---

# 📚 Lessons Learned

- AST-based dependency extraction is significantly more reliable than string parsing.
- Deterministic analysis should precede AI reasoning.
- Separating parsers, services, and APIs results in a cleaner and more maintainable architecture.
- Early architectural decisions reduce future refactoring effort.

---

# ✅ Status

**Sprint 3 Completed**

Repository Intelligence Engine successfully implemented and integrated into the Cognisys backend.

---

# Day 4 — Software Knowledge Graph Development

**Sprint:** Sprint 05 – Software Knowledge Graph Engine  
**Status:** ✅ Completed

---

# Objective

The primary objective for Day 4 was to move beyond repository metadata and build the core infrastructure required for representing software projects as a **Knowledge Graph**. This lays the groundwork for future architecture analysis, AI reasoning, and interactive visualizations.

---

# Work Completed

## Knowledge Graph Foundation

Designed and implemented the core graph models used throughout Cognisys.

Implemented components:

- Node
- Edge
- KnowledgeGraph
- NodeType
- RelationshipType

These structures provide a standardized way to represent software entities and their relationships.

---

## Entity Extraction

Developed an Entity Extractor to traverse repository contents and convert them into graph nodes.

Current supported entities include:

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

## Relationship Extraction

Implemented automatic relationship generation between repository entities.

Current supported relationship:

- `contains`

This establishes the structural hierarchy of a repository inside the knowledge graph.

---

## Graph Builder

Implemented a centralized Graph Builder responsible for constructing a complete Software Knowledge Graph from extracted entities and relationships.

Responsibilities include:

- Aggregating graph nodes
- Creating graph edges
- Producing a unified graph representation

---

## Graph Serialization

Developed a Graph Serializer for exporting the Knowledge Graph into JSON format.

This enables seamless integration with:

- AI Reasoning Engine
- Visualization frameworks
- Graph databases
- Reporting modules

---

## Intelligent File Classification

Introduced an intelligent file classification engine capable of identifying software roles based on repository conventions.

Current classifications:

- Python File
- Service
- Documentation
- Configuration
- Technology
- Workflow

This improves semantic understanding compared to simple file extension detection.

---

# Testing

Successfully validated:

- Graph creation
- Entity extraction
- Relationship generation
- Graph serialization
- File classification

All generated graph structures were successfully serialized into JSON.

---

# Challenges Faced

- Refined graph model design to support future AI reasoning.
- Improved entity extraction by excluding unnecessary directories such as `.git`, `__pycache__`, and virtual environments.
- Enhanced node typing to better represent software architecture.

---

# Outcome

By the end of Day 4, Cognisys evolved from a repository analyzer into a platform capable of constructing a structured **Software Knowledge Graph**.

This graph now serves as the central data model for future modules including:

- Software Architecture Intelligence
- Dependency Analysis
- AI-powered Repository Chat
- Interactive Graph Visualizations

---

# Progress

Sprint 05 Progress:

- ✅ Knowledge Graph Models
- ✅ Entity Extraction
- ✅ Relationship Extraction
- ✅ Graph Builder
- ✅ Graph Serializer
- ✅ Intelligent File Classification

Overall Sprint Completion: **~80%**
