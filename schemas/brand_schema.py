from pydantic import BaseModel

class Brand(BaseModel):
    id: int
    brand: str

    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand
        }