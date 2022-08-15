import math

import numpy as np
import pandas as pd

from fastapi.testclient import TestClient


def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given the payload make a prediction
    payload = {
        # ensure pydantic plays well with np.nan - Else make them None
        "inputs": test_data.replace({np.nan: None}).to_dict(orient="records")
    }

    # Get Response from our API
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload
    )

    # Test succeeds iff we get a prediction
    # Add more tests to more edge cases the complicated the API gets
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["predictions"]
    assert prediction_data["errors"] is None
    assert math.isclose(prediction_data["predictions"][0], 113422, rel_tol=100)