from datetime import datetime
from uuid import UUID
from strawberry import input, type


@type
class Class:
  id: UUID
  name: str
  academic_year: str
  created_at: datetime
  updated_at: datetime
  
@input
class CreateClassInput:
  name: str
  academic_year: str