from sqlalchemy import Column, Integer, String, Float, Date, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PendingQuery(Base):
    __tablename__ = 'pending_query'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    request_status = Column(Integer)
    request_date = Column(Date)


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


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
        