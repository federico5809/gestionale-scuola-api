from strawberry import field, type
from uuid import UUID

from app.api.graphql.context import Info
from .types import Student

@type
class StudentQuery():
  
  @field
  async def get_student_by_id(self, info: Info, id: UUID) -> Student:
    student_service = info.context.student_service
    
    return await student_service.get_by_id(id)