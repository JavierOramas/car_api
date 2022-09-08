from pydantic import BaseModel

class Model(BaseModel):
    id: int
    model: str
    brand: int

    def serialize(self):
        return {
            'id': self.id,
            'model': self.model,
            'brand': self.brand
        }