from strawberry import field, type
from uuid import UUID

from app.api.graphql.context import Info
from .types import Class


@type
class ClassQuery:

    @field
    async def get_class(self, info: Info, id: UUID) -> Class | None:
        class_service = info.context.class_service

        db_class = await class_service.get_by_id(id)
        if not db_class:
            return None

        return db_class