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


# Development Day 5

**Project:** Cognisys  
**Sprint:** Sprint 6 – Software Architecture Intelligence  
**Developer:** Harsh Aryan  
**Duration:** Full Day Development

---

# Objective

Today's objective was to transform Cognisys from a repository parser into a complete Software Architecture Intelligence Engine capable of understanding software architecture, dependency relationships, architectural patterns, risk areas, and generating architectural reports automatically.

---

# Modules Completed

## 1. Circular Dependency Detector

### Objective

Detect circular dependencies inside the repository using graph traversal.

### Implementation

- Implemented Depth First Search (DFS)
- Maintained visited nodes
- Maintained recursion stack
- Maintained traversal path
- Detected back edges
- Extracted dependency cycles
- Eliminated duplicate cycles

### Features

- Detects direct cycles
- Detects indirect cycles
- Supports multiple independent cycles
- Returns detected dependency paths

### Testing

Performed testing using:

- Manual dependency graph
- Cognisys repository dependency graph

Result

```
No circular dependencies found.
```

Repository passed the architecture validation.

---

## 2. Hotspot Detector

### Objective

Identify highly coupled modules inside the repository.

### Implementation

Calculated

- Fan-In
- Fan-Out
- Coupling Score
- Risk Level

Risk Classification

- HIGH
- MEDIUM
- LOW

Ignored

- __init__.py modules
- Internal package initialization files

### Top Repository Hotspots

Examples

- graph_models
- repository_service
- main.py
- repository_cloner
- analysis_service

### Outcome

Successfully ranked repository modules according to architectural importance.

---

## 3. Architecture Pattern Detector

### Objective

Automatically identify the architecture used by the repository.

### Implemented Patterns

- Layered Architecture
- MVC
- Monolithic Architecture

### Detection Logic

Uses

- Layer Detector
- Dependency Graph

Generated

- Confidence Score
- Supporting Evidence

### Output

Detected

- Layered Architecture
- MVC
- Monolithic Architecture

---

## 4. Recommendation Engine

### Objective

Generate architectural recommendations based on repository analysis.

### Inputs

- Hotspots
- Circular Dependencies
- Architecture Patterns

### Generated Recommendations

Examples

- Reduce coupling
- Split large services
- Preserve layer separation
- Consider modularization

Recommendations include

- Priority
- Module
- Recommendation
- Title

---

## 5. Report Generator

### Objective

Generate architecture reports.

### Supported Formats

- JSON
- Markdown

Generated Reports

```
reports/
    architecture_report.json
    architecture_report.md
```

The reports contain

- Hotspots
- Architecture Patterns
- Circular Dependencies
- Recommendations

---

## 6. Architecture Engine

### Objective

Create a single orchestration engine that executes the complete architecture pipeline.

### Pipeline

Repository

↓

Layer Detection

↓

Dependency Graph

↓

Circular Dependency Detection

↓

Hotspot Detection

↓

Architecture Pattern Detection

↓

Recommendation Generation

↓

Report Generation

### Output

Single API

```python
ArchitectureEngine().analyze(repository)
```

Returns

- Layers
- Dependency Graph
- Circular Dependencies
- Hotspots
- Architecture Patterns
- Recommendations
- Report Paths

---

# Testing Performed

Successfully tested

- Circular Dependency Detector
- Hotspot Detector
- Architecture Pattern Detector
- Recommendation Engine
- Report Generator
- Architecture Engine

Verified

- JSON Report Generation
- Markdown Report Generation
- Complete Pipeline Execution

No critical runtime issues encountered.

---

# Technical Concepts Used

- Graph Theory
- Depth First Search (DFS)
- Dependency Analysis
- Fan-In Analysis
- Fan-Out Analysis
- Coupling Analysis
- Architectural Pattern Recognition
- Repository Analysis
- Report Serialization
- Dataclasses
- Software Architecture Intelligence

---

# Files Created

```
app/architecture/

circular_dependency_detector.py
hotspot_detector.py
architecture_models.py
architecture_pattern_detector.py
recommendation_models.py
recommendation_engine.py
report_generator.py
architecture_engine.py
```

---

# Test Files Created

```
test_circular_dependency_detector.py

test_hotspot_detector.py

test_architecture_pattern_detector.py

test_recommendation_engine.py

test_report_generator.py

test_architecture_engine.py
```

---

# Sprint Progress

```
Sprint 6

████████████████████████████████████████████████████████████████████████

Completed

✔ Entry Point Detector

✔ Layer Detector

✔ Service Detector

✔ Dependency Graph

✔ Circular Dependency Detector

✔ Hotspot Detector

✔ Architecture Pattern Detector

✔ Recommendation Engine

✔ Report Generator

✔ Architecture Engine
```

---

# Outcome

Today's development completed the Software Architecture Intelligence layer of Cognisys.

The system is now capable of

- Understanding repository architecture
- Building dependency graphs
- Detecting architectural risks
- Identifying software architecture patterns
- Producing engineering recommendations
- Exporting architecture reports
- Executing a complete end-to-end architecture analysis pipeline

Sprint 6 has been successfully completed.

---

# Next Development

Sprint 7 – AI Architecture Intelligence

Planned Features

- RAG Pipeline
- Vector Database
- Repository Chat
- Semantic Search
- Architecture Question Answering
- Impact Analysis
- Root Cause Analysis
- AI Repository Assistant
- LLM Integration
- Intelligent Architecture Insights

---

**Status:** ✅ Development Day 5 Completed Successfully

---

# Development Log — 02 August 2026

## Project
**Cognisys – AI Repository Intelligence Platform**

---

# Objective

Today's goal was to transform Cognisys from a document-based RAG prototype into a fully local AI-powered Repository Intelligence Assistant using Ollama while improving the repository knowledge pipeline.

---

# Completed Tasks

## 1. Knowledge Document Generation

Enhanced the Knowledge Document Generator by extending repository analysis outputs.

### Newly Generated Documents

- architecture.md
- repository_summary.md
- hotspots.md
- architecture_patterns.md
- recommendations.md
- dependency_graph.md
- services.md
- apis.md
- technologies.md

The generator now produces structured AI-readable knowledge documents for every repository analysis.

---

## 2. Dependency Graph Documentation

Implemented automatic dependency graph documentation.

Features

- Module dependency summary
- Dependency count
- Imported modules
- Repository dependency statistics

Output

```
storage/documents/dependency_graph.md
```

---

## 3. Service Detection

Implemented automatic service detection.

Detected

- Services
- API Routers
- API Endpoints
- Controllers

Generated

```
services.md
```

---

## 4. API Documentation Generation

Added automatic API documentation generation.

Includes

- HTTP Method
- Function Name
- Source File

Generated

```
apis.md
```

---

## 5. Technology Detection

Implemented repository technology detection.

Automatically detects

- Programming Languages
- Frameworks
- Databases
- Machine Learning Libraries
- Deployment Technologies

Generated

```
technologies.md
```

---

## 6. Multi Document Chunking

Completed AI chunk generation for all knowledge documents.

Pipeline

```
Knowledge Documents
        ↓
Chunk Generator
        ↓
Chunk Metadata
        ↓
Storage
```

Features

- Metadata preservation
- Chunk numbering
- Word statistics
- Title extraction

---

## 7. Multi Embedding Generation

Generated embeddings for every repository knowledge chunk.

Embedding Model

```
sentence-transformers/all-MiniLM-L6-v2
```

Embedding Dimension

```
384
```

---

## 8. Multi Vector Store

Implemented FAISS-based vector indexing.

Features

- Multi-document indexing
- Metadata storage
- Similarity search
- Fast retrieval

Indexed

```
296 repository chunks
```

---

## 9. Multi Semantic Search

Implemented repository-wide semantic retrieval.

Supports

- Natural language queries
- Multi-document retrieval
- Similarity ranking
- Context retrieval

---

## 10. Prompt Builder V2

Implemented structured prompt generation.

Prompt Structure

- System Instructions
- Repository Context
- User Question
- AI Response

This significantly improved repository-specific responses.

---

## 11. Ollama Integration

Successfully migrated from cloud LLMs to local inference.

Installed

- Ollama
- qwen2.5-coder:7b
- llama3.1:8b

Configured

```
LLM_PROVIDER=ollama
LLM_MODEL=qwen2.5-coder:7b
```

Benefits

- Unlimited local inference
- Offline support
- Zero API costs
- No quota limitations

---

## 12. Multi Provider LLM Engine

Refactored the LLM engine into a provider-independent architecture.

Supported Providers

- Ollama
- Gemini
- OpenAI

Current Default

```
Ollama
```

---

## 13. Repository Chat Testing

Validated the complete RAG pipeline.

Verified

- Repository retrieval
- Context generation
- Prompt building
- Local LLM inference
- Repository question answering

Example Queries

- Where is repository cloning implemented?
- Describe backend architecture.
- Explain architecture layers.
- Which APIs are available?
- What technologies are used?

---

# Issues Encountered

### Gemini API

- Deprecated model versions
- API quota limitations
- Resource exhausted errors

Resolution

Migrated to Ollama.

---

### OpenAI

- API billing requirement
- Paid usage model

Resolution

Removed as the primary development provider.

---

### Ollama Performance

Observation

Repository responses were slower than expected.

Analysis

- Running entirely on CPU
- Large prompt size
- Large retrieval context

Planned Improvements

- Hybrid Retrieval
- Query Classification
- Dynamic Top-K
- Prompt Builder V3
- Response Streaming

---

# Current Repository AI Pipeline

```
Repository

      │

Repository Analysis

      │

Knowledge Documents

      │

Chunk Generation

      │

Embedding Generation

      │

FAISS Vector Database

      │

Semantic Search

      │

Prompt Builder

      │

Ollama (Local LLM)

      │

Repository Intelligence
```

---

# Project Statistics

Knowledge Documents

```
9
```

Repository Chunks

```
296
```

Embedding Dimension

```
384
```

LLM

```
qwen2.5-coder:7b
```

Vector Database

```
FAISS
```

Inference

```
Local (Offline)
```

---

# Next Sprint Tasks

- Hybrid Retriever
- Repository Overview Generator
- Prompt Builder V3
- Conversation Memory
- Source Citation
- Streaming Responses
- GitHub Repository Analyzer
- FastAPI Chat API
- React Chat Interface

---

# Progress Summary

Sprint Progress

```
█████████████████████░░░ 90%
```

Completed

- Repository Analysis
- Knowledge Generation
- AI Knowledge Base
- Chunking
- Embeddings
- Vector Database
- Semantic Search
- Prompt Builder
- Local LLM Integration
- Repository Chat

Current Status

Cognisys is now capable of performing end-to-end repository intelligence using a fully local Retrieval-Augmented Generation (RAG) pipeline powered by Ollama. The system can analyze software repositories, generate structured knowledge documents, retrieve relevant contextual information, and answer repository-specific questions without relying on external cloud APIs.


# Development Log

**Project:** Cognisys – AI-Powered Repository Intelligence Platform  
**Author:** Harsh Aryan  
**Date:** 05 August 2026  
**Sprint:** Sprint 7 – RAG Engine Completion

---

# Objective

Continue building the Retrieval-Augmented Generation (RAG) engine by improving response quality, citation support, answer formatting, conversation handling, and performance monitoring.

---

# Modules Completed

## Citation Engine

Implemented a dedicated citation system responsible for generating repository references from retrieved knowledge.

### Features

- Extract citations from Hybrid Retriever results
- Remove duplicate citations
- Sort citations using hybrid retrieval score
- Markdown formatting
- Plain text formatting
- Console display support

### Files

```
app/ai/citation_engine.py
test_citation_engine.py
```

---

## Answer Formatter

Implemented a response formatter that converts raw LLM responses into structured repository answers.

### Features

- Cleans generated responses
- Formats repository answers
- Adds repository source section
- Markdown output
- Plain text output
- Formatting statistics
- Console display

### Files

```
app/ai/answer_formatter.py
```

---

## Performance Monitor

Implemented a lightweight execution profiler for the complete RAG pipeline.

### Features

- Start timer
- Stop timer
- Measure execution stages
- Generate timing reports
- Display performance statistics
- Calculate total execution time

### Files

```
app/ai/performance_monitor.py
```

---

## Configuration Review

Reviewed the application configuration layer.

Current files

```
app/core/constants.py
app/core/settings.py
app/core/logger.py
```

Verified:

- Environment loading
- Project constants
- Storage paths
- Logging configuration

Planned improvements:

- AI configuration variables
- File logging
- Centralized defaults

---

# Testing

Successfully tested

- Citation Engine
- Conversation Memory
- Repository Overview Generator
- Hybrid Retriever
- Prompt Builder V3
- RAG Pipeline
- Performance Monitor

---

# Architecture Progress

Current AI Pipeline

```
Repository
      │
      ▼
Knowledge Generation
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Semantic Search
      │
      ▼
Hybrid Retrieval
      │
      ▼
Repository Overview
      │
      ▼
Prompt Builder V3
      │
      ▼
Conversation Memory
      │
      ▼
LLM Engine
      │
      ▼
Citation Engine
      │
      ▼
Answer Formatter
      │
      ▼
Final Response
```

---

# Sprint 7 Progress

Completed

- Repository Knowledge Generation
- Multi Document Chunking
- Multi Embedding Generation
- FAISS Vector Store
- Multi Semantic Search
- Query Classifier
- Hybrid Retriever
- Repository Overview Generator
- Prompt Builder V3
- Conversation Memory
- RAG Pipeline
- Citation Engine
- Answer Formatter
- Performance Monitor

Current Progress

```
Sprint 7 Progress

███████████████████████████████████░

≈ 98%
```

---

# Remaining Tasks

- Improve logging system
- Strengthen error handling
- Integrate Citation Engine into RAG Pipeline
- Integrate Answer Formatter into RAG Pipeline
- Integrate Performance Monitor into RAG Pipeline

---

# Next Sprint

Sprint 8

Backend Development

Planned modules

- FastAPI application
- Chat API
- Repository Upload API
- Memory API
- Health Check API
- Repository Analysis API

---

# Notes

Today's development focused on polishing the AI engine rather than introducing new retrieval algorithms.

The repository now supports:

- Structured prompt generation
- Hybrid retrieval
- Repository-aware citations
- Professional answer formatting
- Conversation memory
- Execution performance monitoring

The remaining effort before Sprint 8 primarily involves integrating these utilities into the production pipeline and exposing them through a FastAPI backend.
