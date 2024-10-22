# Backend - Machine Learning API with JWT Authentication

This backend API is built using **FastAPI** for machine learning model management and **JWT** token-based authentication.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Endpoints](#endpoints)
- [Usage](#usage)

## Features
- Train machine learning models (e.g., Decision Trees, Random Forest) with hyperparameter tuning using GridSearchCV.
- Predict outcomes with the trained models.
- JWT authentication for secure access to the API.

## Requirements
- Python 3.8 or later
- FastAPI
- Uvicorn
- scikit-learn
- Python-Jose (for JWT encoding/decoding)

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd backend
    ```

2. **Set up a virtual environment (if using conda)**:
    If you haven't already created a conda environment:
    ```bash
    conda create -n ml-api python=3.11
    conda activate ml-api
    ```

3. **Install the dependencies**:

    If you have the `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

    To generate `requirements.txt` manually, you can use:
    ```bash
    pip freeze > requirements.txt
    ```

4. **Running the API**:
    To start the FastAPI server using Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```

    The server will be running on `http://127.0.0.1:8000/` by default.

## Environment Variables

In the `config.py` file, you will need to specify some environment variables by creating .env file:

- **SECRET_KEY**: Your secret key for JWT token generation.
- **TOKEN_EXPIRE_IN_MINUTES**: Time (in minutes) for which a token will be valid.

You can hardcode these values or set them using environment variables.

## Endpoints

### 1. `/request_token` - POST
   - **Description**: Authenticates a user and returns a JWT token.
   - **Request body**:
     - `username`: User's username
     - `password`: User's password.
   - **Response**: Returns a JWT token.

### 2. `/train` - POST
   - **Description**: Train a machine learning model with specified algorithm and hyperparameters.
   - **Request body**: 
     - `algorithm`: Specify either "decision_tree" or "random_forest".
     - `params`: Optional hyperparameters for model tuning.
   - **Response**: Best parameters and model score after training.

### 3. `/predict` - POST
   - **Description**: Predict based on input data using the trained model.
   - **Request body**:
     - Input features.
   - **Response**: Predicted class.

## Usage

1. **JWT Authentication**:
   First, you'll need to get a token by sending a POST request to `/request_token` with the username and password in the body. Example using Postman:

   - **URL**: `http://localhost:8000/request_token`
   - **Method**: POST
   - **Body**: `raw (JSON)`
     - `username`: `test_1`
     - `password`: `testpassword`

   The response will contain a token. Use this token to access other endpoints by adding it to the `Authorization` header as a `Bearer Token`.

2. **Train a Model**:
   Send a POST request to `/train` with the selected algorithm and optional hyperparameters in the body.

3. **Predict with a Model**:
   Once the model is trained, you can use the `/predict` endpoint to make predictions.