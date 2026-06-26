from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Studente
# TOBEFIXED = l'import non viene eseguito correttamente perchè negli schemas manca il file __init__.py con gli export del modulo
# sistemato
from app.schemas import CreateStudent


class StudentService():

    def __init__(self, model: Studente, db_session: AsyncSession):
        self.model = model
        self.db = db_session

    async def list_students(self, class_id: UUID | None = None):

        query = select(self.model) # seleziona model student per preparare la query

        if class_id is not None: # verifica se è stato chiesto un class_id
            query = query.where(self.model.class_id == class_id)
            # se non viene richiesto nulla, class_id = None
            # se sì, vengono selezionati gli studenti solo di quella classe

        result = await self.db.execute(query) # SQLAlchemy invia la query al database

        return result.scalars().all()
            # scalars prende gli studenti selezionati
            # all li raggruppa in una lista

    async def create(self, obj_in: CreateStudent) -> Studente: # per creare un nuovo studente nel database
        data = obj_in.model_dump(exclude_unset=True)
        db_obj = self.model(**data)
        self.db.add(db_obj)
        await self.db.flush()
        await self.db.refresh(db_obj)
        return db_obj