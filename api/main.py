from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Fintexa Demo API"}

@app.get("/health")
def health_check():
    return {"status": "[OK]", "service": "demo-api", "env": os.getenv("ENV", "unknown")}