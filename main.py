from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Characteristic(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

cars_db: List[Car] = []

@app.get("/ping")
def ping():
    return "pong"

@app.post("/cars", status_code=status.HTTP_201_CREATED)
def create_car(car: Car):
    cars_db.append(car)
    return car

@app.get("/cars")
def get_cars():
    return cars_db

@app.get("/cars/{id}")
def get_car(id: str):
    for car in cars_db:
        if car.identifier == id:
            return car
    raise HTTPException(status_code=404, detail="Car not found")
