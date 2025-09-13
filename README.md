# FastAPI Demo Project

A demo FastAPI application showcasing best practices for project structure.

## Project Structure

```
fast-api-demo/
├── app/                    # Main application package
│   ├── __init__.py
│   ├── main.py             # FastAPI app instance and startup
│   ├── settings.py         # Configuration settings
│   ├── api/                # API routes
│   │   ├── __init__.py
│   │   ├── api_v1/         # API version 1
│   │   │   ├── __init__.py
│   │   │   ├── api.py      # API router
│   │   │   └── endpoints/  # API endpoints
│   │   │       ├── __init__.py
│   │   │       └── items.py
│   ├── core/               # Core functionality
│   │   ├── __init__.py
│   │   ├── config.py       # Configuration management
│   │   └── database.py     # Database connection
│   ├── models/             # Data models
│   │   ├── __init__.py
│   │   └── item.py
│   ├── schemas/            # Pydantic schemas
│   │   ├── __init__.py
│   │   └── item.py
│   └── utils/              # Utility functions
│       ├── __init__.py
│       └── helpers.py
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_main.py
│   └── api/
│       ├── __init__.py
│       └── test_items.py
├── static/                 # Static files
├── scripts/                # Utility scripts
│   └── init_db.py
├── .gitignore
├── pyproject.toml          # Project configuration
└── uv.lock                 # Dependency lock file
```

## Features

- RESTful API with CRUD operations
- SQLAlchemy ORM integration
- Pydantic models for data validation
- Configurable settings
- Comprehensive test suite
- Static file serving
- Custom Swagger UI and ReDoc documentation

## Installation

1. Install dependencies:
   ```bash
   pip install -e .
   ```

2. Initialize the database:
   ```bash
   python scripts/init_db.py
   ```

## Running the Application

```bash
uvicorn app.main:app --reload
```

Or run directly:
```bash
python app/main.py
```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

Run tests with pytest:
```bash
pytest
