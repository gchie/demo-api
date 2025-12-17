from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "[OK]", "service": "demo-api", "env": os.getenv("ENV", "unknown")}