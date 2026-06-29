from uuid import UUID, uuid4
from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from .base_model import BaseModel
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .classe import Classe

class Professore(BaseModel):
    __tablename__ = "professore"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)

    name: Mapped[str] = mapped_column(String)
    subject: Mapped[str] = mapped_column(String)

    classe_insegnante: Mapped[List["Classe"]] = relationship(
        "Classe",
        back_populates="professore"
    )

    voti = relationship("voto", back_populates="professore_")