from fastapi import FastAPI
from routers.car_router import router as car_router
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["car_api_db"]

app = FastAPI()

app.include_router(car_router)
