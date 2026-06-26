from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Professore
# TOBEFIXED = l'import non viene eseguito correttamente perchè negli schemas manca il file __init__.py con gli export del modulo
from app.schemas import CreateProfessor


class ProfessorService():

    def __init__(self, model: Professore, db_session: AsyncSession):
        self.model = model
        self.db = db_session

    async def list_professors(self):
        result = await self.db.execute(select(self.model))
        return result.scalars().all() # restituisce i professori

    async def create(self, obj_in: CreateProfessor) -> Professore: # nuovo professore...
        data = obj_in.model_dump(exclude_unset=True)
        db_obj = self.model(**data)
        self.db.add(db_obj)
        await self.db.flush()
        await self.db.refresh(db_obj)
        return db_obj