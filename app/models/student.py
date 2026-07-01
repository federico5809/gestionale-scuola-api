from uuid import UUID
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .classroom import Class

from .base_model import BaseModel


class Student(BaseModel):
    __tablename__ = "students"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)

    nome: Mapped[str] = mapped_column(String)
    cognome: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)

    class_id: Mapped[UUID] = mapped_column(ForeignKey("classes.id"))

    classe_frequentante: Mapped["Class"] = relationship("Class", back_populates="students")
    voti = relationship("Grade", back_populates="student")