from uuid import UUID, uuid4
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .classe import Classe

from .base_model import BaseModel


class Studente(BaseModel):
    __tablename__ = "studente"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)

    nome: Mapped[str] = mapped_column(String)
    cognome: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)

    class_id: Mapped[UUID] = mapped_column(ForeignKey("classe.id"))

    classe_frequentante: Mapped["Classe"] = relationship(
        "Classe",
        back_populates="studenti"
    )

    voti = relationship(
        "voto",
        back_populates="studente_valutato"
    )