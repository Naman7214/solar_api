from fastapi import FastAPI, UploadFile, File, HTTPException, Request, status
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from app.config.settings import settings
import tensorflow as tf
from app.routes.prediction_route import router as prediction_router
from app.routes.get_description_route import router as description_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Your existing API routes below...
app.include_router(prediction_router, prefix="/api/v1")
app.include_router(description_router, prefix="/api/v1")
