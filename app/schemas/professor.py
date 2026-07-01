from pydantic import BaseModel

class BaseProfessor(BaseModel):
    name: str
    last_name: str
    subject: str

class CreateProfessor(BaseProfessor):
    pass