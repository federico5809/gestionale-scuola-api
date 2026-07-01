from strawberry import mutation, type, asdict

from app.api.graphql.context import Info

from .types import CreateClassInput, Class
#CORRETTO = import da CreateClasse a CreateClass
from app.schemas.classroom import CreateClass

from uuid import UUID

@type
class ClassMutation():
    
    @mutation
    async def class_create(self, info: Info, input: CreateClassInput) -> Class:
        #CORRETTO = da class_service a class_services
        class_services = info.context.class_service
        obj_in = CreateClass(**asdict(input))
        return await class_services.create(obj_in)

    @mutation
    async def assign_professor_to_class(
        self, 
        info: Info, 
        professor_id: UUID, 
        class_id: UUID
    ) -> bool:
        class_services = info.context.class_service
        # Chiamata al servizio per collegare i due ID sulla tabella Many-to-Many
        return await class_services.assign_professor(professor_id=professor_id, class_id=class_id)