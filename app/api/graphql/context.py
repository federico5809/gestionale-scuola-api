from dataclasses import dataclass
from fastapi import Request
from strawberry.fastapi import BaseContext
from strawberry.types import Info as SBInfo

from app.services import student_service, professor_services, class_services

@dataclass
class Context(BaseContext):
    request: Request
    student_service: student_service
    professor_services: professor_services
    class_services: class_services

Info = SBInfo[Context, None]