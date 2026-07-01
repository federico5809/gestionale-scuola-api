from .student import CreateStudent
#CORRETTO = naming di CreateProfessor e CreateClass
from .professor import CreateProfessor
from .classroom import CreateClass
from .grade import CreateGrade
# TOBEFIXED: gli export e gli import non corrispondono
__all__ = [
    "CreateStudent",
    "CreateProfessor",
    "CreateClass",
    "CreateGrade"
]