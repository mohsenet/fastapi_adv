# File: api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
