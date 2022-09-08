from pydantic import BaseModel

class Car(BaseModel):
    id: int
    brand: str
    model: str
    generation: str
    description: str
    doors: int
    passengers: int
    fuel_eco: str

    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'generation': self.generation,
            'description': self.description,
            'doors': self.doors,
            'passengers': self.passengers,
            'fuel_eco': self.fuel_eco
        }