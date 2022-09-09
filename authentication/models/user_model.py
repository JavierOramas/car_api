from pydantic import BaseModel
class User(BaseModel):
    name: str
    password: str
    api_key: str
    roles: list[str]
    requests: int
    registration_date: str
    api_expiration_date: str
    
    def serialize(self):
        return {
            'name': self.name,
            'password': self.password,
            'api_key': self.api_key,
            'roles': self.roles,
            'requests': self.requests,
            'registration_date': self.registration_date,
            'api_expiration_date': self.api_expiretion_date
        }