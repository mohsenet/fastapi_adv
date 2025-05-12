from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from scipy.stats import norm

app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate_gaussian")
def generate_gaussian(mean: float = 0, std_dev: float = 1, size: int = 1000):
    """Generate Gaussian distribution data"""
    data = np.random.normal(loc=mean, scale=std_dev, size=size).tolist()
    return {
        "data": data,
        "mean": float(np.mean(data)),
        "std_dev": float(np.std(data))
    }

@app.get("/calculate_density")
def calculate_density(x: float, mean: float = 0, std_dev: float = 1):
    """Calculate probability density at point x"""
    density = norm.pdf(x, loc=mean, scale=std_dev)
    return {
        "x": x,
        "density": float(density),
        "mean": mean,
        "std_dev": std_dev
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
