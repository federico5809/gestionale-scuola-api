from uuid import UUID
from pydantic import BaseModel

class BaseClasse(BaseModel):
    name: str
    academic_year: str

class CreateClasse(BaseClasse):
    pass