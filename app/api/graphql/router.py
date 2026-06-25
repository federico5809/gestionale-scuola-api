from fastapi import Depends, Request # work in progress
from strawberry import type, Schema
from strawberry.extensions import QueryDepthLimiter
from strawberry.fastapi import GraphQLRouter

from app.api.graphql.context import Context
from app.services import student_services 
from app.services import professor_services, professor_service
from app.services import class_services, get_class_services

from .student import queries, StudentQuery, StudentMutation, mutations
from .professor import queries, mutations
from .classe import queries, mutations

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
) -> Context:
    return Context(
        request=request,
        animal_service=animal_service,
        person_service=person_service
    )

graphQLRouter = GraphQLRouter(schema=schema, context_getter=get_context)