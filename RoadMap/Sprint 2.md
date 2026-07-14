# Sprint 2 — Repository Clone Engine

**Project:** Cognisys  
**Sprint Duration:** Day 2  
**Status:** ✅ Completed

---

# 🎯 Sprint Goal

Develop the Repository Clone Engine to enable Cognisys to fetch GitHub repositories, manage local repository storage, and provide a reliable foundation for repository analysis.

---

# 📌 Objectives

- Implement GitHub repository cloning
- Design repository storage mechanism
- Build repository service layer
- Create Repository Clone API
- Handle invalid repository URLs
- Improve Windows compatibility
- Implement repository caching
- Establish storage directory structure

---

# 🏗 System Architecture

```text
                 GitHub Repository
                         │
                         ▼
                Repository Clone API
                         │
                         ▼
               Repository Service Layer
                         │
                         ▼
              Repository Cloner Engine
                         │
                         ▼
             Local Repository Storage
```

---

# 📂 Components Added

```text
backend/
│
├── app/
│   │
│   ├── parser/
│   │   └── repository_cloner.py
│   │
│   ├── services/
│   │   └── repository_service.py
│   │
│   ├── schemas/
│   │   └── repository.py
│   │
│   └── api/
│       └── v1/
│           └── repository.py
│
└── storage/
    └── temp/
```

---

# ✅ Features Implemented

## 1. Repository Clone Engine

Implemented a Git-based cloning engine using GitPython.

Responsibilities:

- Clone public GitHub repositories
- Store repositories locally
- Return repository metadata
- Handle cloning failures

---

## 2. Repository Service

Created a service layer responsible for orchestrating repository operations.

Responsibilities:

- Validate repository requests
- Call cloning engine
- Return structured responses
- Separate business logic from API layer

---

## 3. Repository Clone API

Implemented REST endpoint.

Endpoint:

```http
POST /api/v1/repositories/clone
```

Input

```json
{
    "repository_url": "https://github.com/user/project.git"
}
```

Response

```json
{
    "repository_name": "project",
    "local_path": "storage/temp/project"
}
```

---

## 4. Repository Schemas

Implemented request and response validation using Pydantic.

Models:

- RepositoryRequest
- RepositoryResponse

Benefits:

- Automatic validation
- Better documentation
- Strong typing

---

## 5. Local Repository Storage

Created storage architecture.

```text
storage/

└── temp/

    └── repository_name/
```

Repositories are stored locally for future analysis.

---

## 6. Repository Caching

Improved cloning strategy.

Instead of deleting repositories every request,

Cognisys now:

```text
Repository Exists?

        │

   Yes ─────────► Use Cached Repository

        │

   No

        ▼

 Clone Repository
```

Benefits:

- Faster execution
- Reduced network traffic
- Avoids Windows file-lock issues
- Better user experience

---

## 7. Error Handling

Implemented structured error handling.

Handled cases:

- Invalid repository URL
- Git clone failure
- Existing repositories
- Missing directories

---

# 🧠 Engineering Decisions

## Service-Oriented Architecture

Separated cloning logic from API.

```text
API

↓

Repository Service

↓

Repository Cloner

↓

GitPython
```

This improves testability and maintainability.

---

## Repository Caching

Repositories are reused instead of deleted.

Advantages:

- Faster repeated analysis
- Lower bandwidth usage
- Prevents Windows permission errors
- Production-friendly behavior

---

## Temporary Storage

Repositories are isolated inside:

```text
storage/temp/
```

Future versions will support automatic cleanup and persistent caching.

---

# 📦 Technologies Used

Backend

- Python
- FastAPI

Git Integration

- GitPython

Validation

- Pydantic

Utilities

- pathlib
- logging
- shutil

---

# 📊 Sprint Deliverables

| Feature | Status |
|----------|--------|
| Repository Clone Engine | ✅ |
| Repository Service | ✅ |
| Repository API | ✅ |
| Repository Schemas | ✅ |
| Local Storage | ✅ |
| Repository Caching | ✅ |
| Error Handling | ✅ |

---

# 🚀 Sprint Outcome

At the end of Sprint 2, Cognisys was capable of cloning public GitHub repositories, storing them locally, and exposing repository cloning through a structured REST API.

This established the foundation required for repository intelligence and software analysis in subsequent sprints.

---

# 📚 Lessons Learned

- Service layers improve separation of concerns.
- Repository caching is more efficient than repeated cloning.
- Windows file systems require careful handling of Git directories.
- Pydantic simplifies request validation and API documentation.

---

# 📈 Sprint Progress

```text
Repository Clone Engine

████████████████████████████████

100% Completed
```

---

# 🎯 Next Sprint

**Sprint 3 — Repository Intelligence**

Planned objectives:

- Repository Scanner
- Technology Detection
- Dependency Analysis
- Architecture Analysis
- Repository Metadata Extraction
- Foundation for AI Reasoning
