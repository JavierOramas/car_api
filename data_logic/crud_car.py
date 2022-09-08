from schemas.car_schema import Car
from schemas.brand_schema import Brand
from schemas.model_schema import Model
from starlette.responses import FileResponse
from data_logic import crud_brand, crud_model


def get_car(db, brand:str, model:str):
    brand = crud_brand.get_brand(db, brand)
    model = crud_model.get_model_brand(db, model, brand)
    if model:
        car = db.Car.find({'brand': brand['id'],'model': model['id']}) 
        return car
    return None


def get_image(db, brand:str, model:str):
    car = get_car(db, brand, model)
    if not car:
        return None
    return FileResponse(car.image, media_type='image/png')