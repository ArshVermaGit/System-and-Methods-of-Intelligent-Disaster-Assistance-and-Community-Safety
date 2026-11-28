import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Intelligent Disaster Assistance & Community Safety API",
    description=(
        "Backend API for flood and landslide risk assessment, "
        "hazard segmentation, and community safety."
    ),
    version="0.1.0",
)

# CORS Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "project": "System and Methods of Intelligent Disaster Assistance and Community Safety",
        "phase": "EPICS Phase I",
        "status": "operational",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "backend",
        "environment": os.getenv("ENVIRONMENT", "development"),
    }
