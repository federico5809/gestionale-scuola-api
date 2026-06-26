from fastapi import Depends, Request
from strawberry import type, Schema
from strawberry.extensions import QueryDepthLimiter
from strawberry.fastapi import GraphQLRouter

from app.api.graphql.context import Context
from app.services.professor_services import ProfessorService, get_professor_service
from app.services.student_services import StudentService, get_student_service
from app.services.class_services import ClassService, get_class_service

from .student import StudentQuery, StudentMutation
from .professor import ProfessorQuery, ProfessorMutation
from .classe import ClassQuery, ClassMutation

@type
class Query(StudentQuery, ProfessorQuery, ClassQuery):
    pass

@type
class Mutation(StudentMutation, ProfessorMutation, ClassMutation):
    pass

schema = Schema(query=Query, mutation=Mutation, extensions=[
    QueryDepthLimiter(max_depth=6)
])

async def get_context(
    request: Request,
    professor_service: ProfessorService = Depends(get_professor_service),
    student_service: StudentService = Depends(get_student_service),
    class_service: ClassService = Depends(get_class_service),
) -> Context:
    return Context(
        request = request,
        professor_service = professor_service,
        student_service = student_service,
        class_service = class_service
    )
graphQLRouter = GraphQLRouter(schema=schema, context_getter=get_context)