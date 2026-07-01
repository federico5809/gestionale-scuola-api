#CORRETTO = tolto import UUID non necessario
from pydantic import BaseModel

class BaseClass(BaseModel):
    name: str
    academic_year: str

class CreateClass(BaseClass):
    pass