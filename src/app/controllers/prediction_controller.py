from fastapi import Depends, HTTPException, status
from src.app.usecases.prediction_usecase import PredictionUsecase

class PredictionContoller:
    def __init__(self, usecase: PredictionUsecase = Depends()):
        self.usecase = usecase

    async def prediction_controller(self, image_path: str):
        try:
            prediction = await self.usecase.prediction_usecase(image_path)
            return prediction
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=str(e)
            )