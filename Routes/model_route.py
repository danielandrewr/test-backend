from fastapi import APIRouter, Depends, HTTPException
from Model.model import model
from Auth.token_handler import verify_token
from Schema.model_schema import ModelTrain, Predict

router = APIRouter()

@router.post("/train")
def train(request: ModelTrain, token: str = Depends(verify_token)):
    """
    Train the machine learning model with the specified algorithm and hyperparameters.

    Parameters:
        request (ModelTrain): The algorithm and hyperparameter grid.

    Returns:
        JSON response with the best parameters and score from grid search.
    """
    algorithm = request.algorithm
    params = request.param_grid

    try:
        res = model.train(algorithm, params)
        return {
            "message": "Successfully trained model.",
            "best_params_": res["best_params"],
            "best_score": res["best_score"]
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=e)
    
@router.post('/predict')
def predict(request: Predict, token: str = Depends(verify_token)):
    """
    Make a prediction using the trained machine learning model.

    Parameters:
        request (Predict): The input data (features) for prediction.

    Returns:
        JSON response with the predicted class.
    """
    input = request.input

    try:
        res = model.predict(input)
        return {"prediction": int(res[0])}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=e)

@router.get('/status')
def fetch_status(token: str = Depends(verify_token)):
    """
    Get the current status of the model, including whether it's trained and
    the details of the trained model (e.g., best parameters, algorithm).

    Returns:
        JSON response with the model's status.
    """
    print(f"Token: {token}")
    return model.fetch_status()