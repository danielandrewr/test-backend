from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Routes import auth_route, model_route

# FastAPI Instance
app = FastAPI() 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_route.router)
app.include_router(model_route.router)
