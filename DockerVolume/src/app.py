from fastapi import FastAPI, Request
import logging
import os
from datetime import datetime

# Ensure 'logs' directory exists
os.makedirs("logs", exist_ok=True)

# Setup logging
log_filename = datetime.now().strftime("logs/app_%Y-%m-%d.log")
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logging.info(f"Completed response: {response.status_code}")
    return response

@app.get("/")
def read_root():
    logging.info("Root endpoint accessed")
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    logging.info(f"/items/{item_id} accessed with query: {q}")
    return {"item_id": item_id, "query": q}
