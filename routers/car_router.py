import imp
from sqlite3 import Cursor
from fastapi import APIRouter, Depends, HTTPException
from schemas.car_schema import Car
from schemas.brand_schema import Brand
from schemas.model_schema import Model
from typing import List
from sqlalchemy.orm import Session
from data_logic import crud_car, crud_brand, crud_model
from dependencies import close_db, get_db, get_current_user

router = APIRouter(
    prefix='/car',
    tags=['car'],
    responses={404: {'description': 'Not found'}}
)

# Create
@router.post('/', response_model=Brand)
def create_brand(brand: Brand):
    db = get_db()
    return crud_brand.create_brand(db,brand)

@router.post('/model', response_model=Model)
def create_model(model: Model):
    db = get_db()
    return crud_model.create_model(db,model)

@router.post('/car', response_model=Car)
def create_car(car: Car):
    db = get_db()
    return crud_car.create_car(db,car)

#  Read 
@router.get('/', response_model=List[Brand])
def get_brands():

    db = get_db()

    values = list(crud_brand.get_all_brands(db))

    if len(values) == 0:
        raise HTTPException(status_code=404, detail='No brands found')

    return values

@router.get('/{brand}', response_model=List[Model])
def get_models(brand: str):

    db = get_db()

    values = list(crud_model.get_all_models_brand(db, brand))
    print(list(values))

    if len(values) == 0:
        raise HTTPException(status_code=404, detail='Brand not found')

    return values

@router.get('/{brand}/{model}', response_model=Car)
def get_car(brand: str, model: str):

    db = get_db()

    value = crud_car.get_car(db, brand, model)

    if not value:
        raise HTTPException(status_code=404, detail='Car not found')

    return value

@router.get('/image/{brand}/{model}')
def get_image(brand: str, model: str):
    db = get_db()

    value = crud_car.get_image(db, brand, model)

    if not value:
        raise HTTPException(status_code=404, detail='Image for Car not found')

    return value
