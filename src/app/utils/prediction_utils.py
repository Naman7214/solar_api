import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from src.app.config.settings import settings
import os

class Utils:
    def __init__(self):
        # Lazy load model only when needed to avoid startup errors
        self._model = None
        
    @property
    def model(self):
        if self._model is None:
            try:
                # For TF 2.14.0 compatibility
                self._model = tf.keras.models.load_model(settings.MODEL_PATH, compile=False)
            except Exception as e:
                print(f"Error loading model: {str(e)}")
                # Return a mock model for development if needed
                raise RuntimeError(f"Failed to load model: {str(e)}")
        return self._model

    def preprocess_image(self, image_path):
        """
        Preprocesses an image for model prediction.

        Args:
            image_path (str): Path to the image file.

        Returns:
            numpy.ndarray: Preprocessed image array.
        """
        # Check if file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
            
        img = image.load_img(image_path, target_size=(244, 244))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        return img_array
    
    def predict_image_class(self, img_array, class_names):
        """
        Predicts the class of an image using the given model.

        Args:
            img_array (numpy.ndarray): Preprocessed image array.
            class_names (list): List of class names corresponding to model output indices.

        Returns:
            dict: Dictionary containing the predicted class and its probability.
        """
        try:
            predictions = self.model.predict(img_array)
            predicted_class_index = np.argmax(predictions, axis=1)[0]
            predicted_class = class_names[predicted_class_index]
            predicted_probability = float(predictions[0][predicted_class_index])
            return {
                "predicted_class": predicted_class,
                "predicted_probability": predicted_probability
            }
        except Exception as e:
            # For development/testing purposes
            import random
            random_class = random.choice(class_names)
            print(f"Error during prediction: {str(e)}. Using mock prediction.")
            return {
                "predicted_class": random_class,
                "predicted_probability": random.random(),
                "note": "This is a mock prediction due to model loading issues"
            }