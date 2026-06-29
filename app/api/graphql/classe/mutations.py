from strawberry import mutation, type, asdict

from app.api.graphql.context import Info

from .types import CreateClassInput, Class
from app.schemas.classe import CreateClasse

from uuid import UUID

@type
class ClassMutation():
    
    @mutation
    async def class_create(self, info: Info, input: CreateClassInput) -> Class:
        class_services = info.context.class_services
        obj_in = CreateClasse(**asdict(input))
        return await class_services.create(obj_in)

    @mutation
    async def assign_professor_to_class(
        self, 
        info: Info, 
        professor_id: UUID, 
        class_id: UUID
    ) -> bool:
        class_services = info.context.class_services
        # Chiamata al servizio per collegare i due ID sulla tabella Many-to-Many
        return await class_services.assign_professor(professor_id=professor_id, class_id=class_id)