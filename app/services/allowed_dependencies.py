from fastapi import Depends
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from core import db

from app.models.studente import Studente
from app.services.student_services import StudentService

from app.models.professore import Professore
from app.services.professor_services import ProfessorService

from app.models.classe import Classe
from app.services.class_services import ClassService

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with db.get_session() as session:
        yield session
    
# -------- DB SERVICES --------
def get_student_service(session: AsyncSession = Depends(get_db_session)) -> StudentService:
    return StudentService(Studente, session)
def get_professor_service(session: AsyncSession = Depends(get_db_session)) -> ProfessorService:
    return ProfessorService(Professore, session)
def get_class_service(session: AsyncSession = Depends(get_db_session)) -> ClassService:
    return ClassService(Classe, session)