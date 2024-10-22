from pydantic import BaseModel
from typing import List, Dict

# Train Data Model needed to train the model
class ModelTrain(BaseModel):
    algorithm: str
    param_grid: Dict[str, List]

# Prediction Data Model
class Predict(BaseModel):
    input: List[float]