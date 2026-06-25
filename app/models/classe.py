from uuid import UUID, uuid4
from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from .base_model import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .studente import Studente
    from .professore import Professore


class Classe(BaseModel):
    __tablename__ = "classe"

    id: Mapped[UUID] = mapped_column(Uuid,primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    academic_year: Mapped[str] = mapped_column(String(9))
    professore_id: Mapped[UUID] = mapped_column(ForeignKey("professore.id"))

    studenti: Mapped[List["Studente"]] = relationship(
        "Studente",
        back_populates="classe_frequentante"
    )

    professore: Mapped["Professore"] = relationship(
        "Professore",
        back_populates="classi"
    )