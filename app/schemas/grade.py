from pydantic import BaseModel
from uuid import UUID

class CreateGrade(BaseModel):
    voto: int
    student_id: UUID
    professor_id: UUID