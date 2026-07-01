from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.schemas import CreateClass
from app.models import Class


class ClassService():

    def __init__(self, model: Class, db_session: AsyncSession):
        self.model = model
        self.db = db_session

    async def get_class(self, id: UUID):
        result = await self.db.execute(
            select(self.model)
            .options(
                selectinload(self.model.studenti), # Carica studenti
                selectinload(self.model.professore) # Carica professori
            )
            .where(self.model.id == id)
        )
        return result.scalar_one_or_none()

    async def create(self, obj_in: CreateClass) -> Class:
        data = obj_in.model_dump(exclude_unset=True)
        db_obj = self.model(**data)
        self.db.add(db_obj)
        await self.db.flush()
        await self.db.refresh(db_obj)
        return db_obj
    
    async def assign_professor(self, professor_id: UUID, class_id: UUID) -> bool:
        # OTTIMIZZAZIONE: Carichiamo la classe caricando SOLO i professori associati (senza studenti)
        result_class = await self.db.execute(
            select(self.model)
            .options(selectinload(self.model.professore))
            .where(self.model.id == class_id)
        )
        class_obj: Class = result_class.scalar_one_or_none()
        
        if not class_obj:
            return False
            
        # Recuperiamo il professore
        from app.models.professor import Professore
        result_prof = await self.db.execute(select(Professore).where(Professore.id == professor_id))
        professor_obj = result_prof.scalar_one_or_none()
        
        if not professor_obj:
            return False
            
        # Append sulla relazione Many-to-Many
        if professor_obj.id != class_obj.professore_id:
            class_obj.professore.append(professor_obj)
            await self.db.flush()
            
        return True