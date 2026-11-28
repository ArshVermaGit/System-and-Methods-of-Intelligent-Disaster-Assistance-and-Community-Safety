# Backend Services (FastAPI)

FastAPI-powered REST APIs for geospatial hazard analysis, risk scoring, and data serving.

## Running Locally

Run commands from the **repository root**:

```bash
uvicorn backend.app.main:app --reload --port 8000
```

> **Note on Project Structure:** The assignment's legacy command `uvicorn app.main:app` is replaced by `uvicorn backend.app.main:app` executed from the repository root. A compatibility shim is also available at `backend.main:app`.

Access API Documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
