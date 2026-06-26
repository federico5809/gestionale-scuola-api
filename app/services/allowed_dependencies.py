from fastapi import Depends # work in progress
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from core import db

from app.models.studente import Studente
# TOBEFIXED = l'import non viene eseguito correttamente perchè il nome non è corretto
from app.services.student_service import StudentService

from app.models.professore import Professore
from app.services.professor_services import ProfessorService

from app.models.classe import Classe
from app.services.class_services import ClassService

async def get_db_session() -> AsyncGenerator[AsyncSession]:
    async with db.get_session() as session:
        yield session
    
# -------- DB SERVICES --------
def get_student_service(session: AsyncSession = Depends(get_db_session)) -> StudentService:
    return StudentService(Studente, session)
def get_professor_service(session: AsyncSession = Depends(get_db_session)) -> ProfessorService:
    return ProfessorService(Professore, session)
def get_class_service(session: AsyncSession = Depends(get_db_session)) -> ClassService:
    return ClassService(Classe, session)