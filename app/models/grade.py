from sqlalchemy import Column, Integer, ForeignKey
from uuid import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.types import Uuid
from .base_model import Base

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Uuid, primary_key=True, index=True) # Usiamo Uuid coerentemente con gli altri modelli
    voto = Column(Integer, nullable=False)
    
    # Verifica se i nomi tabella sono "studente" e "professore" al singolare
    student_id = Column(Uuid, ForeignKey("students.id"), nullable=False)
    professor_id = Column(Uuid, ForeignKey("professors.id"), nullable=False)

    # Relazioni
    student = relationship("Student", back_populates="grades")
    professor = relationship("Professor", back_populates="grades")