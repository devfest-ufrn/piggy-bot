from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Gasto(Base):
    __tablename__ = 'gasto'
    id = Column(Integer, primary_key=True)
    texto = Column(String)
    valor = Column(Integer)


class TipoGasto(Base):
    __tablename__ = 'tipo_gasto'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)
