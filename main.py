from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Location(BaseModel):
    lat: float
    lng: float

def search_shops(lat: float, lng: float):
    return [
        {"name": "Example Shop A", "lat": lat + 0.006, "lng": lng + 0.001},
        {"name": "Example Shop B", "lat": lat - 0.001, "lng": lng - 0.001},
    ]

@app.post("/shops")
def get_shops(loc: Location):
    """
    loc is parsed from the JSON body into a Location object.
    We call search_shops and return its result as JSON.
    """
    return search_shops(loc.lat, loc.lng)
