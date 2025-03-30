from fastapi import FastAPI, Depends
from app.config.settings import settings
from app.utils.prediction_utils import Utils

class PredictionService:
    def __init__(self, utils: Utils = Depends(Utils)):
        self.utils = utils
        self.class_names = settings.CLASS_NAMES

    async def get_prediction(self, image_path: str):
        """
        Get prediction for the given image path.

        Args:
            image_path (str): Path to the image file.

        Returns:
            dict: Dictionary containing the predicted class and its probability.
        """
        img_array = self.utils.preprocess_image(image_path)
        prediction = self.utils.predict_image_class(img_array, self.class_names)
        return prediction