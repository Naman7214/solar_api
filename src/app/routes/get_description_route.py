from fastapi import APIRouter

router = APIRouter()

@router.get("/description")
async def get_description():
    return {
        "API_Description": "This API predicts panel conditions based on uploaded images.",
        "Usage_Guide": [
            "Use the /api/v1/predict endpoint to upload an image file and receive a prediction.",
            "The endpoint requires a multipart/form-data file upload."
        ],
        "More_Info": "Ensure your MODEL_PATH environment variable points to a valid TensorFlow model."
    }