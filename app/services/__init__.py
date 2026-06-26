from .allowed_dependencies import get_student_service
from .allowed_dependencies import get_professor_service
from .allowed_dependencies import get_class_service

from .student_services import StudentService
from .professor_services import ProfessorService
from .class_services import ClassService

__all__ = [
  "StudentService",
  "get_student_service",

  "ProfessorService",
  "get_professor_service",

  "ClassService",
  "get_class_service"
]