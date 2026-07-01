from fastapi import Depends
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
#CORRETTO = import in app.core import db
from app.core import db

from app.models import Student, Professor, Class, Grade
from app.services import StudentService, ProfessorService, ClassService, GradeService

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with db.get_session() as session:
        yield session
    
# -------- DB SERVICES --------
def get_grade_service(session: AsyncSession = Depends(get_db_session)) -> GradeService:
    return GradeService(Grade, session)

def get_student_service(session: AsyncSession = Depends(get_db_session)) -> StudentService:
    return StudentService(Student, session)

def get_professor_service(session: AsyncSession = Depends(get_db_session)) -> ProfessorService:
    return ProfessorService(Professor, session)

def get_class_service(session: AsyncSession = Depends(get_db_session)) -> ClassService:
    return ClassService(Class, session)