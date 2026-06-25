from datetime import datetime
from uuid import UUID
from strawberry import input, type

  
@type
class Professor:
  id: UUID
  name: str
  subject: str
  created_at: datetime
  updated_at: datetime
  
@input
class CreateProfessorInput:
  name: str
  subject: str