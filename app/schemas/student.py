from pydantic import BaseModel

class BaseStudent(BaseModel):
    name: str
    last_name: str
    email: str

class CreateStudent(BaseStudent):
    pass