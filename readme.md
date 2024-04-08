# FastAPI Cerbos

## Overview

FastAPI with Cerbos

## Key Features
- **Structured API Versioning**: Efficient module organization for scalability.
- **Database Integration**: Seamless SQLAlchemy and Alembic integration.
- **Asynchronous Task Handling**: Celery for background task management.
- **Docker and Kubernetes-Ready**: Streamlined deployment and scalability.
- **Healthcheck Endpoints**: For real-time application monitoring.
- **Cerbos Integration**: Robust authentication and authorization.

## Contents

- [Setup and Running](#setup-and-running)
- [API Versioning](#api-versioning)
- [Healthcheck Endpoints](#healthcheck-endpoints)
- [SQLAlchemy and Alembic Integration](#sqlalchemy-and-alembic-integration)
- [Celery Integration](#celery-integration)
- [Pre-Commit Integration](#pre-commit-integration)
- [Dockerfile Explanation](#dockerfile-explanation)
- [Cerbos Integration](#cerbos-integration)

## Setup and Running

### Initial Setup

- **Poetry for Dependency Management**: Install with `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`.
- **Docker and Docker Compose**: Essential for containerization. Follow the official Docker website for installation.
- **Starting Services**: Use `docker compose up` for DB and RabbitMQ.

### Running the Server

- **Uvicorn**: `uvicorn main:app --reload` for development.

### Managing Dependencies

- **Adding/Removing Packages**: Use `poetry add <package-name>` and `poetry remove <package-name>`.

## API Versioning

### Structure

- **Resource-based Directory**: `cms` directory signifies a resource group.
- **Organized By Functionality**: Utilities, helpers, and DB methods under `cms/videos`.
- **CRUD Operations**: Located in `crud.py`.
- **Helpers and Models**: In `helpers.py` and `models.py` respectively.
- **Background Tasks**: Handled in `tasks.py`.

### Version Specifics

- **Routes and Schemas Versioning**: In `v1` for easy API version management.
- **Separation of Concerns**: `crud.py` for DB operations, `routes.py` for endpoints.

## Healthcheck Endpoints

- **Simple Monitoring**: Defined in `healthcheck/routes.py`.

## SQLAlchemy and Alembic Integration

- **Configuration**: Hosted at `conf/db/`.
- **Models and Dependencies**: Defined in `models.py` and `dependencies.py`.

## Pre-Commit Integration

- **Usage**: Run `pre-commit install`. Linting occurs automatically on commit.

## Dockerfile Explanation

- **Multistage Build**: Efficient setup for smaller and faster builds.
- **Production Ready**: Tested for production environments.

## Cerbos Integration

### Generating JWT Tokens

- **For Users**: `python scripts/generate_jwt.py 'test@google.com' '["user"]' '{"region":"eu-east-1"}'`.
- **For Managers/Admins**: Similar command, replace role with `"manager"` or `"admin"`.
- **For Auditing**: `python scripts/generate_jwt.py 'auditor@google.com' '["user"]' '{"region":"eu-east-1"}'`.

> The region is hardcoded to "eu-east-1" in the script and the server, if we want to generate a token with a
> different location. We can simply change the location and that would work. Also, the JWT tokens generated are
> just the dummy tokens, also the JWT tokens are not stored in the database, they are just generated on the fly.
> Same goes for the REST Endpoints, the resources are not stored in the database, they are just dummy resources.
> But we can use the actual resources and the JWT tokens to test the REST Endpoints.

### Testing REST Endpoints

- **GET for Read Permission**: `GET: http://localhost:8000/api/v1/cms/videos/123/`
- **PATCH for Update Permission**: `PATCH: http://localhost:8000/api/v1/cms/videos/123/`
- **DELETE for Delete Permission**: `DELETE: http://localhost:8000/api/v1/cms/videos/123/`

The inclusion of Cerbos significantly enhances the security and scalability of FastAPI ProKit, making it an ideal choice for modern web application development.
All the endpoints need the JWT Token in the Authorization Header to be tested.
```
docker run --rm --name cerbos -t \
  -v ./tests:/tests \
  -v ./policies:/policies \
  -p 3592:3592 \
  ghcr.io/cerbos/cerbos:latest compile --tests=/tests /policies
```


Step 1: In terminal 1
`uvicorn main:app --reload`

Step 2: In terminal 2
`docker compose up -d`

Step 3: In terminal 3
EU user:

Generate JWT Token
`python scripts/generate_jwt.py 'test@google.com' '["user"]' '{"region":"eu-east-1"}'`

Check Access
`curl -v -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJDZXJib3MiLCJzdWIiOiJ0ZXN0QGdvb2dsZS5jb20iLCJleHAiOjE3MTI2MTA0MTIsImlhdCI6MTcxMjUyNDAxMiwicm9sZXMiOlsidXNlciJdLCJpZCI6IjhlZDAyNTY5LTg2MjItNGZiMi04NTA5LTE3ZjA3NTVhNjM4OSIsImF0dHIiOnsicmVnaW9uIjoiZXUtZWFzdC0xIn19.9XmXXJZvZBWsJX6zbOedHJ17bpks-23_6Mu-dT4bZ-Q" http://localhost:8000/api/v1/cms/videos/123/`

`curl -v -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJDZXJib3MiLCJzdWIiOiJ0ZXN0QGdvb2dsZS5jb20iLCJleHAiOjE3MTIyMTk5MjAsImlhdCI6MTcxMjEzMzUyMCwicm9sZXMiOlsidXNlciJdLCJpZCI6Ijg4NDk0NGQwLTVmOTYtNDgzNC04ZDIxLTgyY2NjMTQwNmQ5MCIsImF0dHIiOnsicmVnaW9uIjoidXMtZWFzdC0xIn19.svI4N3z78YnsnxwWzuuztDs-aRUjJh5OSVjwOihX7J8" http://localhost:8000/api/v1/cms/videos/123/`

<!-- 
EU user:
curl -v -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJDZXJib3MiLCJzdWIiOiJ0ZXN0QGdvb2dsZS5jb20iLCJleHAiOjE3MTI1OTQ3NDUsImlhdCI6MTcxMjUwODM0NSwicm9sZXMiOlsidXNlciJdLCJpZCI6IjkxNDYwZTY2LWRhZDMtNDFmYi04ZmMyLWM5MjU1YmNjMDdlZSIsImF0dHIiOnsicmVnaW9uIjoiZXUtZWFzdC0xIn19.f4tgQQhpRsAE-9plVbKhwle8pOqIglWEBCQxJD2-x0c" http://localhost:8000/api/v1/cms/videos/123/

EU-manager:
curl --location --request PATCH 'http://localhost:8000/api/v1/cms/videos/123' \
--header 'Content-Type: application/json' \
--header '"Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJDZXJib3MiLCJzdWIiOiJ0ZXN0QGdvb2dsZS5jb20iLCJleHAiOjE3MTI1OTQ3NDUsImlhdCI6MTcxMjUwODM0NSwicm9sZXMiOlsidXNlciJdLCJpZCI6IjkxNDYwZTY2LWRhZDMtNDFmYi04ZmMyLWM5MjU1YmNjMDdlZSIsImF0dHIiOnsicmVnaW9uIjoiZXUtZWFzdC0xIn19.f4tgQQhpRsAE-9plVbKhwle8pOqIglWEBCQxJD2-x0c' \
--data '{
    "title": "Title",
    "description": "test",
    "marked_done": false,
    "user": 1
}'

curl --location --request PATCH 'http://localhost:8000/api/v1/cms/videos/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJDZXJib3MiLCJzdWIiOiJ0ZXN0QGdvb2dsZS5jb20iLCJleHAiOjE3MTIwNTA4NDQsImlhdCI6MTcxMTk2NDQ0NCwicm9sZXMiOlsibWFuYWdlciJdLCJpZCI6ImExYmU3MzkxLWUwY2QtNGE3Zi05MGM0LTE3YjYwMmRjOTBiOCIsImF0dHIiOnsicmVnaW9uIjoiZXUtZWFzdC0xIn19.2gv2m5sb1IS1__5QDpjjeWQmvgJrIQr0kEE7HMkKY_s' \
--data '{
    "title": "Title",
    "description": "test",
    "marked_done": false,
    "user": 1
}'



US-manager:
curl --location --request PATCH 'http://localhost:8000/api/v1/cms/videos/123' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJDZXJib3MiLCJzdWIiOiJ0ZXN0QGdvb2dsZS5jb20iLCJleHAiOjE3MTIyMjAyNjEsImlhdCI6MTcxMjEzMzg2MSwicm9sZXMiOlsibWFuYWdlciJdLCJpZCI6IjUxNWNlYTA1LTgwYjctNDViNy1iNTEyLTM3NTBiYWUzNTM4MyIsImF0dHIiOnsicmVnaW9uIjoidXMtZWFzdC0xIn19.qSyvuNvJvUmnfmoecuGAe2qOgAhmzYOTHFIflCpAqv0' \
--data '{
    "title": "Title",
    "description": "test",
    "marked_done": false,
    "user": 1
}'


auditor - us - manager
curl --location --request PATCH 'http://localhost:8000/api/v1/cms/videos/123' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJDZXJib3MiLCJzdWIiOiJhdWRpdG9yQGdvb2dsZS5jb20iLCJleHAiOjE3MTIyMjAzMjIsImlhdCI6MTcxMjEzMzkyMiwicm9sZXMiOlsibWFuYWdlciJdLCJpZCI6IjU0MWEzMDU5LWU1MWQtNDIzZi05MTRiLWM1NGI0NzQ2OWNmYiIsImF0dHIiOnsicmVnaW9uIjoidXMtZWFzdC0xIn19.hN0DFTiPjfBTE_OKbgYXRX8K5qHLc-4rqBiMKEZXW4w' \
--data '{
    "title": "Title",
    "description": "test",
    "marked_done": false,
    "user": 1
}'

curl --location --request PATCH 'http://localhost:8000/api/v1/cms/videos/123' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJDZXJib3MiLCJzdWIiOiJhdWRpdG9yQGdvb2dsZS5jb20iLCJleHAiOjE3MTIyMTg2NDEsImlhdCI6MTcxMjEzMjI0MSwicm9sZXMiOlsiYXVkaXRvciJdLCJpZCI6IjI1OWE2NDA4LTMxYTQtNDI5Yi04YWVkLTFhNWM0ZThkNzdmNSIsImF0dHIiOnsicmVnaW9uIjoidXMtZWFzdC0xIn19.4t8PnAvWCEi56vPwnxsWgAh3sX6zNuxYzrKcsvM8l_g' \
--data '{
    "title": "Title",
    "description": "test",
    "marked_done": false,
    "user": 1
}'
 -->

