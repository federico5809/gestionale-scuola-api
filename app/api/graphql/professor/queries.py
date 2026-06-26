from strawberry import field, type
from uuid import UUID

from app.api.graphql.context import Info
from .types import Professor


@type
class ProfessorQuery:

    @field
    async def list_professors(self, info: Info) -> list[Professor]:
        professor_service = info.context.professor_service
        return await professor_service.list_professors()

    @field
    async def get_professor_by_id(self, info: Info, id: UUID) -> Professor | None:
        professor_service = info.context.professor_service
        # TOBEFIXED = il controllo puoi eseguirlo direttamente nel service professor_service aggiungendo una clusula where
        professors = await professor_service.list_professors()

        for professor in professors:
            if professor.id == id:
                return professor

        return None