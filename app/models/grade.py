from sqlalchemy import Column, Integer, ForeignKey
from uuid import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.types import Uuid
from app.core.__init__ import Base  # Assicurati che Base sia l'istanza corretta di declarative_base

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Uuid, primary_key=True, index=True) # Usiamo Uuid coerentemente con gli altri modelli
    voto = Column(Integer, nullable=False)
    
    # Verifica se i nomi tabella sono "studente" e "professore" al singolare
    student_id = Column(Uuid, ForeignKey("studente.id"), nullable=False)
    professor_id = Column(Uuid, ForeignKey("professore.id"), nullable=False)

    # Relazioni
    # Assicurati che in studente.py ci sia grades = relationship("Grade", back_populates="studente_valutato")
    studente_valutato = relationship("Studente", back_populates="grades")
    
    # Allineato con voti = relationship("voto", back_populates="professore_") visto prima
    professore_ = relationship("Professore", back_populates="voti")