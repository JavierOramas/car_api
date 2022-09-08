from schemas.brand_schema import Brand

def create_brand(db, brand: Brand):
    db_brand = get_brand(db, brand.brand)
    if db_brand:
        return db_brand
    return db.Brand.insert_one(brand.dict())

def get_brand(db, brand_name:str):
    db_brand = db.Brand.find_one({'brand': brand_name})
    if db_brand:
        return Brand(**db_brand)
    return None

def get_brand_by_id(db, brand_id:int):
    db_brand = db.Brand.find_one({'id': brand_id})
    if db_brand:
        return Brand(**db_brand)
    return None

def get_all_brands(db):
    brands = db.Brand.find()
    if brands:
        return brands
    return []