# Solar API

## Project Overview
A FastAPI application that predicts solar panel conditions using a TensorFlow model.

## Setup Instructions
1. Clone the repository or download the code.
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Add a .env file with model path and environment variables:
    ```env
    MODEL_PATH="/path/to/model.keras"
    ```

## Running the Project
Start the application using:
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```
## Access the API
The API will be served at [http://localhost:8000](http://localhost:8000).

- Use `/api/v1/predict` to upload an image and get a prediction.
- Use `/api/v1/description` to get the API description.

## Additional Notes
- The default class names are defined in `app/config/settings.py`.
- Logs or error messages will appear in the console if the model fails to load.
- Adjust the `allow_origins` parameter in `main.py` if you want to allow requests from other sources.

