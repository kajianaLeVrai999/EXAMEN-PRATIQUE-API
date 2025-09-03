from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

class CarModel (BaseModel):
    identifier : str
    brand : str
    modele : str
    characteristics : object

cars_list : List[CarModel] = []

@app.post("/cars")
def new_cars(car_playload: List[CarModel]):
    cars_list.extend(car_playload)
    return {"cars": new_cars}

@app.get("/cars")
def list_cars():
    return {"cars" : cars_list}
