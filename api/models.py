from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Expense(Base):
    __tablename__ = 'expense'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    value = Column(Float)


class ExpenseCategory(Base):
    __tablename__ = 'expense_category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
