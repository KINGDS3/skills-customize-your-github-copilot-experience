# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice routing, request validation, response handling, and automatic API documentation. Students will design endpoints for a simple resource and learn how modern Python web frameworks structure an API.

## 📝 Tasks

### 🛠️ Project Setup and Data Model

#### Description
Create a FastAPI application with a clear project entry point and a simple in-memory data model for one resource, such as books, tasks, or students.

#### Requirements
Completed program should:

- Create a FastAPI app that runs with `uvicorn`
- Define a Pydantic model for the resource data
- Store records in memory using a list or dictionary
- Include at least one example record to test against

### 🛠️ Create Read Endpoints

#### Description
Add endpoints that let clients fetch all records and fetch a single record by ID.

#### Requirements
Completed program should:

- Implement `GET /items` to return all records
- Implement `GET /items/{item_id}` to return one record
- Return a `404` response when the requested record does not exist
- Return JSON responses with predictable field names

### 🛠️ Add Write Endpoints and Validation

#### Description
Add endpoints that let clients create and update records, then make sure invalid data is rejected cleanly.

#### Requirements
Completed program should:

- Implement `POST /items` to create a new record
- Implement `PUT /items/{item_id}` or `PATCH /items/{item_id}` to update an existing record
- Validate request bodies using FastAPI and Pydantic
- Return the appropriate status codes for created and updated resources
- Show the API in the interactive docs at `/docs`