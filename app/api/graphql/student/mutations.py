from strawberry import mutation, type, asdict

from app.api.graphql.context import Info

from .types import CreateStudentInput, Student
from app.schemas.student import CreateStudent

@type
class StudentMutation():

  @mutation
  async def student_create(self, info: Info, input: CreateStudentInput) -> Student:
    student_service = info.context.student_service
    
    obj_in = CreateStudent(**asdict(input))

    return await student_service.create(obj_in)