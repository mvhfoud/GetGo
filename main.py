from fastapi import FastAPI
from pydantic import BaseModel
import requests

# 1. Create the FastAPI “app” instance
app = FastAPI()

# 2. Define the shape of incoming data
class Location(BaseModel):
    lat: float
    lng: float

# 3. Your core function: look up shops (here we just return a stub)
def search_shops(lat: float, lng: float):
    # 👉 Replace this stub with real API calls later
    return [
        {"name": "Example Shop A", "lat": lat + 0.001, "lng": lng + 0.001},
        {"name": "Example Shop B", "lat": lat - 0.001, "lng": lng - 0.001},
    ]

# 4. Expose it as a POST endpoint at /shops
@app.post("/shops")
def get_shops(loc: Location):
    """
    loc is parsed from the JSON body into a Location object.
    We call search_shops and return its result as JSON.
    """
    return search_shops(loc.lat, loc.lng)
