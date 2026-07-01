from strawberry import mutation, type, asdict

from app.api.graphql.context import Info

from .types import CreateProfessorInput, Professor
from app.schemas.professor import CreateProfessore

@type
class ProfessorMutation():

  @mutation
  async def professor_create(self, info: Info, input: CreateProfessorInput) -> Professor:
    professor_services = info.context.professor_services
    
    obj_in = CreateProfessore(**asdict(input))

    return await professor_services.create(obj_in)