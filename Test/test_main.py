from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_train():
    payload = {
        "algorithm": "random_forest",
        "param_grid": {
            "n_estimators": [50, 100],
            "max_depth": [5, 10]
        }
    }
    
    response = client.post("/train", json=payload)
    
    assert response.status_code == 200
    
    response_json = response.json()
    assert "best_params" in response_json
    assert "best_score" in response_json

def test_predict():
    payload = {
        "algorithm": "random_forest",
        "param_grid": {
            "n_estimators": [50, 100],
            "max_depth": [5, 10]
        }
    }
    client.post("/train", json=payload)

    predict_payload = {
        "input": [5.1, 3.5, 1.4, 0.2]
    }
    
    response = client.post("/predict", json=predict_payload)
    
    assert response.status_code == 200

    response_json = response.json()
    assert "prediction" in response_json

def test_status():
    response = client.get("/status")
    
    assert response.status_code == 200
    
    response_json = response.json()
    assert "is_trained" in response_json