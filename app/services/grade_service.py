from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Grade
from app.schemas import CreateGrade
from uuid import UUID

class GradeService:
    def __init__(self, model: Grade, db_session: AsyncSession):
        self.model = model
        self.db = db_session

    async def create(self, obj_in: CreateGrade):
        data = obj_in.model_dump()
        if "voti" in data:
            data["voto"] = data.pop("voti")
            
        db_obj = self.model(**data)
        self.db.add(db_obj)
        await self.db.flush()
        await self.db.refresh(db_obj)
        return db_obj

    async def get_by_student_id(self, student_id: UUID):
        result = await self.db.execute(
            select(self.model).where(self.model.student_id == student_id)
        )
        return result.scalars().all()

    async def get_by_professor_id(self, professor_id: UUID):
        result = await self.db.execute(
            select(self.model).where(self.model.professor_id == professor_id)
        )
        return result.scalars().all()

    async def update(self, grade_id: UUID, voto: int):
        obj = await self.db.get(self.model, grade_id)
        if not obj:
            return None
        obj.voto = voto
        await self.db.flush()
        return obj

    async def delete(self, grade_id: UUID):
        obj = await self.db.get(self.model, grade_id)
        if obj:
            await self.db.delete(obj)
            await self.db.flush()
        return obj