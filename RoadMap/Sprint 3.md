# Sprint 3 — Repository Intelligence Engine

**Project:** Cognisys  
**Sprint Duration:** Day 3  
**Status:** ✅ Completed

---

# 🎯 Sprint Goal

Develop Cognisys' deterministic repository intelligence engine capable of understanding software projects by analyzing their structure, technologies, dependencies, and architectural components without relying on Large Language Models.

---

# 📌 Objectives

- Build Repository Scanner
- Detect project technologies
- Analyze Python dependencies
- Infer repository architecture
- Create deterministic analysis pipeline
- Design modular parser architecture
- Prepare foundation for AI reasoning

---

# 🏗 System Architecture

```text
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
```

---

# 📂 Components Added

```text
backend/
│
├── app/
│   │
│   ├── parser/
│   │   ├── repository_scanner.py
│   │   ├── technology_detector.py
│   │   ├── dependency_analyzer.py
│   │   └── architecture_analyzer.py
│   │
│   └── services/
│       └── repository_service.py
```

---

# ✅ Features Implemented

## 1. Repository Scanner

Implemented a repository scanning engine capable of extracting structural metadata.

### Extracted Information

- Repository name
- Total files
- Total directories
- File extensions
- Configuration files
- Docker files
- Documentation files
- GitHub workflow files
- Largest files
- Empty directories

The scanner creates the structural foundation required for deeper analysis.

---

## 2. Technology Detector

Developed a deterministic technology detection engine.

### Supported Languages

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

Detection is performed by analyzing:

- requirements.txt
- package.json
- pyproject.toml
- Dockerfile

without using AI.

---

## 3. Dependency Analyzer

Implemented dependency extraction using Python's Abstract Syntax Tree (AST).

### Features

- Detects Python imports
- Extracts module relationships
- Ignores comments
- Ignores invalid syntax safely
- Builds dependency mappings

Example

```text
main.py

↓

RepositoryService

↓

RepositoryScanner
```

Using AST ensures significantly higher accuracy compared to regular expression parsing.

---

## 4. Architecture Analyzer

Implemented automatic repository architecture inference.

Current capabilities:

- Backend detection
- Frontend detection
- Full Stack detection
- Docker detection
- GitHub Actions detection
- Database identification

The analyzer provides a high-level architectural overview of the repository.

---

# 🧠 Engineering Decisions

## Deterministic Analysis First

Instead of asking an LLM to understand repositories directly,

Cognisys first performs deterministic software analysis.

Advantages:

- Faster execution
- Explainable results
- Higher reliability
- Lower inference cost

---

## Modular Parser Design

Each parser is responsible for a single concern.

```text
Repository Scanner

↓

Technology Detector

↓

Dependency Analyzer

↓

Architecture Analyzer
```

This design enables future expansion without modifying existing modules.

---

## AST-Based Parsing

Python dependencies are extracted using the built-in AST module rather than string matching.

Benefits:

- Syntax-aware parsing
- Higher accuracy
- Safer analysis
- Easier future extensions

---

# 📦 Technologies Used

Backend

- Python
- FastAPI

Static Analysis

- AST
- pathlib

Repository Analysis

- GitPython

Utilities

- logging
- json
- collections

---

# 📊 Sprint Deliverables

| Feature | Status |
|----------|--------|
| Repository Scanner | ✅ |
| Technology Detector | ✅ |
| Dependency Analyzer | ✅ |
| Architecture Analyzer | ✅ |
| Deterministic Repository Analysis | ✅ |

---

# 🚀 Sprint Outcome

Sprint 3 transformed Cognisys from a repository cloning application into a repository intelligence platform capable of understanding software systems through deterministic analysis.

The project can now:

- Understand repository structure
- Detect technologies
- Analyze dependencies
- Infer software architecture

This forms the foundation for future knowledge graph generation and AI-powered reasoning.

---

# 📚 Lessons Learned

- Deterministic analysis should precede AI reasoning.
- AST parsing is more reliable than text-based parsing.
- Modular parser architecture simplifies maintenance.
- Repository intelligence is more valuable when built incrementally.

---

# 📈 Sprint Progress

```text
Repository Intelligence Engine

████████████████████████████████

100% Completed
```

---

# 🎯 Next Sprint

**Sprint 4 — Unified Analysis Engine**

Planned objectives:

- Analysis Service
- Unified Analysis API
- Repository orchestration
- Single analysis endpoint
- End-to-end repository intelligence pipeline
- Unified JSON response
