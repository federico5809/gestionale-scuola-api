from dataclasses import dataclass
from fastapi import Request
from strawberry.fastapi import BaseContext
from strawberry.types import Info as SBInfo

from app.services import StudentService, ProfessorService, ClassService

@dataclass
class Context(BaseContext):
    request: Request
    student_service: StudentService
    professor_service: ProfessorService
    class_service: ClassService


Info = SBInfo[Context, None]