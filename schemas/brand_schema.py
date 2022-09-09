from pydantic import BaseModel

class Brand(BaseModel):
    id: int
    brand: str
    image: str

    def serialize(self):
        if self.image == None or self.image == '':
            self.image = 'images/brands/default.jpg'
        return {
            'id': self.id,
            'brand': self.brand,
            'image': self.image
        }