from fastapi import Depends
from src.app.services.prediction_service import PredictionService

class PredictionUsecase:
    def __init__(self, service: PredictionService = Depends()):
        self.service = service

    async def prediction_usecase(self,image_path: str):
        return await self.service.get_prediction(image_path)
