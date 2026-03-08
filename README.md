# FastAPI PostgreSQL Docker Starter 🚀

A production-ready REST API built with FastAPI, PostgreSQL, and Docker.
Demonstrates containerized backend development with persistent storage,
environment-based configuration, and SQLAlchemy ORM.

## Tech Stack

- **FastAPI** — Modern Python web framework
- **PostgreSQL 16** — Relational database
- **SQLAlchemy** — ORM for database interaction
- **Docker & Docker Compose** — Containerization
- **Pydantic** — Data validation

## Features

- ✅ Fully containerized — runs anywhere with Docker
- ✅ Persistent database storage via Docker volumes
- ✅ Environment-based configuration via `.env`
- ✅ Auto table creation on startup
- ✅ Health check ensures DB ready before API starts
- ✅ RESTful user management endpoints

## Prerequisites

Only **Docker Desktop** is required.
No Python, no PostgreSQL installation needed.

- [Install Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Quick Start

1. Clone the repository
```bash
   git clone https://github.com/yourusername/fastapi-postgres-docker.git
   cd fastapi-postgres-docker
```

2. Create your environment file
```bash
   cp .env.example .env
```
   Edit `.env` with your values.

3. Start the application
```bash
   docker compose up --build
```

4. Visit the API
   - Swagger UI: http://localhost:8000/docs
   - Health check: http://localhost:8000/

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/users` | Create a new user |
| GET | `/users` | Get all users |

## Project Structure
```
├── app/
│   ├── main.py          # FastAPI app and endpoints
│   ├── database.py      # SQLAlchemy engine and session
│   └── models.py        # Database table definitions
├── .env.example         # Environment variables template
├── .gitignore           # Git ignore rules
├── docker-compose.yml   # Multi-container orchestration
├── Dockerfile           # FastAPI container definition
├── requirements.txt     # Python dependencies
└── README.md            # You are here
```

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `POSTGRES_USER` | PostgreSQL username | `postgres` |
| `POSTGRES_PASSWORD` | PostgreSQL password | `secret123` |
| `POSTGRES_DB` | Database name | `my_db` |
| `DATABASE_URL` | Full connection string | `postgresql://...` |

## Data Persistence

Data persists across container restarts via Docker named volumes.
```bash
# Stop containers (data preserved)
docker compose down

# Stop containers AND delete all data
docker compose down -v
```

## Development

To run with live code reload:
```bash
docker compose up --build
```

Changes to Python files reflect automatically.

## License

MIT License — feel free to use this as a starter template.