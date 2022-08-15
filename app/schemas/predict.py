from typing import Any, List, Optional

from pydantic import BaseModel
from model.processing.validation import DataModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleInputs(BaseModel):
    inputs: List[DataModel]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "v1": 4,
                        "v2": 8,
                        "v3": 15
                    }
                ]
            }
        }