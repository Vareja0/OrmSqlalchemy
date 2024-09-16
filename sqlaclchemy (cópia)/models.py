from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base,relationship, Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import date

from .database import Base

class Flor(Base):
    __tablename__ = "Flores"

    id : Mapped[int] = mapped_column(primary_key=True)
    tipo : Mapped[str]
    cor : Mapped[str]

    compra = relationship("Compra", back_populates="flor")
    

    def __repr__(self) -> str:
        return f"<Flor(id={self.id}, tipo={self.tipo}, cor={self.cor})>"
    
class Compra(Base):
    __tablename__ = "Compras"

    id : Mapped[int] = mapped_column(primary_key=True)
    id_flor : Mapped[int] =  mapped_column(ForeignKey("Flores.id"))
    id_cliente : Mapped[int] = mapped_column(ForeignKey("Clientes.cpf"))
    valor : Mapped[int]
    quantidade : Mapped[int] =  mapped_column(nullable=False)

    flor = relationship("Flor", back_populates="compra")
    cliente = relationship("Cliente", back_populates="compra")

    def __repr__(self) -> str:
        return f"<Flor(id={self.id}, tipo={self.valor}, cor={self.valor})>"
    
class Funcionarios(Base):
    __tablename__ = "Funcionarios"

    cpf: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    data_nasc: Mapped[date]
    tipo: Mapped[str]

    def __repr__(self) -> str:
        return f"<Flor(id={self.cpf}, tipo={self.tipo}, cor={self.nome})>"
    
class Cliente(Base):
    __tablename__ = "Clientes"

    cpf: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]

    compra = relationship("Compra", back_populates="cliente")
    