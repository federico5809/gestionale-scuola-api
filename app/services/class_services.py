from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.schemas import CreateClasse
from app.models import Classe


class ClassService():

    def __init__(self, model: Classe, db_session: AsyncSession):
        self.model = model
        self.db = db_session

    async def get_class(self, id: UUID):

        result = await self.db.execute(
            select(self.model)
            .options(
                selectinload(self.model.studenti), # selectinload carica anche gli studenti e prof collegati
                selectinload(self.model.professori)
            )
            .where(self.model.id == id) # ovviam. dove id corrisponde
        )

        return result.scalar_one_or_none()

    async def create(self, obj_in: CreateClasse) -> Classe: # nuova classe...
        data = obj_in.model_dump(exclude_unset=True)
        db_obj = self.model(**data)
        self.db.add(db_obj)
        await self.db.flush()
        await self.db.refresh(db_obj)
        return db_obj