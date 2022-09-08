from schemas.model_schema import Model
from schemas.car_schema import Car
from schemas.brand_schema import Brand
from data_logic import crud_brand

def create_model(db, model: Model):
    db_model = get_model(db, model.model)
    if db_model:
        return db_model
    print(model)
    # check if id already exists
    db_model = get_model_by_id(db, model.id)
    if db_model:
        return db_model

    try:
        db.Model.insert_one(model.dict())
    except:
        create_model(db, model)
    return model

def get_model(db, model_name:str):
    db_model = db.Model.find_one({'model': model_name})
    if db_model:
        return Model(**db_model)
    return None

def get_model_brand(db, model, brand):
    db_model = db.Model.find_one({'model': model, 'brand': brand})
    if db_model:
        return Model(**db_model)
    return None

def get_model_by_id(db, model_id:int):
    db_model = db.Model.find_one({'id': model_id})
    if db_model:
        return Model(**db_model)
    return None

def get_all_models(db):
    models = db.Model.find()
    if models:
        return models
    return []

def get_all_models_brand(db, brand):
    brand = crud_brand.get_brand(db, brand)
    print(brand.id)
    if brand:
        models = list(db.Model.find({'brand': brand.id}))
        print(models)
        if len(models) != []:
            return models
    return []