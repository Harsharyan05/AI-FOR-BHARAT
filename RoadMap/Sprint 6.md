# Sprint 6 — Software Architecture Intelligence

**Project:** Cognisys  
**Author:** Harsh Aryan

---

# Objective

Build Cognisys into a Software Architecture Intelligence Engine capable of understanding repository structure, architecture, dependencies, coupling, architectural patterns, and generating recommendations and reports.

At the end of Sprint 6, Cognisys should be able to analyze an entire repository and generate an architectural report without any AI assistance.

---

# Sprint Duration

Estimated Duration:
7–10 Days

---

# Sprint Modules

---

## Module 1 — Entry Point Detector

### Goal

Detect application entry files.

### Features

- Detect main.py
- Detect app.py
- Detect __main__.py
- Detect server.py
- Detect manage.py
- Detect run.py
- Detect wsgi.py
- Detect asgi.py

### Output

```python
[
    {
        "file": "main.py",
        "framework": "FastAPI",
        "path": "app/main.py"
    }
]
```

### Status

✅ Completed

---

## Module 2 — Layer Detector

### Goal

Identify software architecture layers.

### Detects

- Presentation
- Business
- Persistence
- Infrastructure
- Analysis
- Knowledge

### Output

```python
{
    "Presentation": [...],
    "Business": [...],
    "Persistence": [...],
    "Infrastructure": [...],
    "Analysis": [...],
    "Knowledge": [...]
}
```

### Status

✅ Completed

---

## Module 3 — Service Detector

### Goal

Detect APIs and services.

### Detects

- FastAPI
- APIRouter
- API Endpoints
- Services

### Output

```python
[
    {
        "type": "API Endpoint",
        "method": "POST",
        "function": "clone_repository"
    }
]
```

### Status

✅ Completed

---

## Module 4 — Dependency Graph

### Goal

Build repository dependency graph.

### Detects

- import
- from ... import ...
- Internal modules
- External modules

### Output

```python
{
    "app.main": [
        "app.api.router",
        "fastapi"
    ]
}
```

### Status

✅ Completed

---

## Module 5 — Circular Dependency Detector

### Goal

Detect circular dependencies.

### Algorithm

Depth First Search (DFS)

### Output

```python
[
    [
        "app.a",
        "app.b",
        "app.c",
        "app.a"
    ]
]
```

### Status

✅ Completed

---

## Module 6 — Hotspot Detector

### Goal

Find highly coupled modules.

### Metrics

- Fan-In
- Fan-Out
- Coupling Score
- Risk

### Output

```python
{
    "module": "app.services.repository_service",
    "fan_in": 2,
    "fan_out": 5,
    "score": 7,
    "risk": "MEDIUM"
}
```

### Status

✅ Completed

---

## Module 7 — Architecture Pattern Detector

### Goal

Identify software architecture.

### Detects

- Layered Architecture
- MVC
- Monolithic Architecture

### Output

```python
{
    "name": "Layered Architecture",
    "confidence": 0.95
}
```

### Status

✅ Completed

---

## Module 8 — Recommendation Engine

### Goal

Generate architectural recommendations.

### Uses

- Hotspots
- Circular Dependencies
- Architecture Patterns

### Output

```python
[
    {
        "priority": "MEDIUM",
        "title": "Medium Coupling",
        "module": "app.services.repository_service",
        "recommendation": "Consider refactoring this module."
    }
]
```

### Status

✅ Completed

---

## Module 9 — Report Generator

### Goal

Generate architecture reports.

### Supported Formats

- JSON
- Markdown

### Output

```
reports/

architecture_report.json

architecture_report.md
```

### Status

✅ Completed

---

## Module 10 — Architecture Engine

### Goal

Orchestrate the entire architecture pipeline.

### Pipeline

Repository

↓

Layer Detector

↓

Dependency Graph

↓

Circular Dependency Detector

↓

Hotspot Detector

↓

Architecture Pattern Detector

↓

Recommendation Engine

↓

Report Generator

↓

Architecture Report

### Output

```python
engine.analyze(repository)
```

Returns

```python
{
    "layers": ...,
    "dependency_graph": ...,
    "cycles": ...,
    "hotspots": ...,
    "patterns": ...,
    "recommendations": ...,
    "json_report": ...,
    "markdown_report": ...
}
```

### Status

✅ Completed

---

# Final Architecture Flow

```
Repository

│

├── Entry Point Detector

├── Layer Detector

├── Service Detector

├── Dependency Graph

├── Circular Dependency Detector

├── Hotspot Detector

├── Architecture Pattern Detector

├── Recommendation Engine

├── Report Generator

└── Architecture Engine
```

---

# Sprint Deliverables

- Entry Point Detection
- Layer Detection
- Service Detection
- Dependency Graph
- Circular Dependency Detection
- Hotspot Detection
- Architecture Pattern Detection
- Recommendation Generation
- JSON Reports
- Markdown Reports
- Complete Architecture Engine

---

# Sprint Outcome

After Sprint 6, Cognisys can:

- Understand repository structure
- Detect architecture layers
- Analyze dependencies
- Detect circular dependencies
- Identify highly coupled modules
- Recognize architecture patterns
- Generate architectural recommendations
- Produce architecture reports
- Execute the complete architecture analysis pipeline through a single engine

---

# Sprint Status

████████████████████████████████████████████████████████████████████████

✅ Sprint 6 Completed

---

# Next Sprint

Sprint 7 — AI Architecture Intelligence

Planned Features

- Repository Q&A
- LLM Integration
- RAG Pipeline
- Semantic Search
- Architecture Explanation
- Root Cause Analysis
- Impact Analysis
- Repository Chat Assistant
- AI-powered Code Understanding
- Interactive Architecture Insights
