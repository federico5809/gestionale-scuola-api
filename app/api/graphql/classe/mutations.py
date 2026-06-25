from strawberry import mutation, type, asdict

from app.api.graphql.context import Info

from .types import CreateClassInput, Class
from app.schemas.classe import CreateClasse

@type
class ClassMutation():

  @mutation
  async def class_create(self, info: Info, input: CreateClassInput) -> Class:
    class_services = info.context.class_services
    
    obj_in = CreateClasse(**asdict(input))

    return await class_services.create(obj_in)