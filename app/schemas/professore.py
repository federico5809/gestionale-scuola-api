from uuid import UUID
from pydantic import BaseModel

class BaseProfessore(BaseModel):
    name: str
    last_name: str
    subject: str

class CreateProfessore(BaseProfessore):
    pass