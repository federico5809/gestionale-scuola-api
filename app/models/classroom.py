from uuid import UUID, uuid4
from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from .base_model import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .student import Student
    from .professor import Professor


class Class(BaseModel):
    __tablename__ = "classes"

    id: Mapped[UUID] = mapped_column(Uuid,primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    academic_year: Mapped[str] = mapped_column(String(9))
    professore_id: Mapped[UUID] = mapped_column(ForeignKey("professors.id"))

    studenti: Mapped[List["Student"]] = relationship("Student", back_populates="classes")
    professore: Mapped["Professor"] = relationship("Professor", back_populates="classes")