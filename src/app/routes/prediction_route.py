from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
import uuid
import os
from app.controllers.prediction_controller import PredictionContoller

router = APIRouter()

@router.post("/predict")
async def predict(
    file: UploadFile = File(...), 
    controller: PredictionContoller = Depends()
):
    # Create uploads directory if it doesn't exist
    upload_dir = "/tmp/solar_api_uploads"
    os.makedirs(upload_dir, exist_ok=True)
    
    file_name = f"{uuid.uuid4()}-{file.filename}"
    file_path = os.path.join(upload_dir, file_name)
    
    # Save the uploaded file
    with open(file_path, "wb") as f:
        content = await file.read()
        if len(content) == 0:
            raise HTTPException(status_code=400, detail="Empty file")
        f.write(content)
    
    try:
        final_results = await controller.prediction_controller(file_path)
        return {"result": final_results}
    finally:
        # Clean up the file
        if os.path.exists(file_path):
            os.remove(file_path)