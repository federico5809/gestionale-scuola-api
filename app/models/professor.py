from uuid import UUID
from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from .base_model import BaseModel
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .classroom import Class

class Professor(BaseModel):
    #nei db le tabelle dovrebbero essere sempre al plurale
    __tablename__ = "professors"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)

    name: Mapped[str] = mapped_column(String)
    subject: Mapped[str] = mapped_column(String)

    classe_insegnante: Mapped[List[Class]] = relationship("Class", back_populates="professor")

    grades = relationship("Grade", back_populates="professor")