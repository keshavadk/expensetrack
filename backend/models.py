

# from sqlalchemy import Column, Integer, String, Float, Date
# from .database import Base

# class Expense(Base):
#     __tablename__ = "expenses"

#     id = Column(Integer, primary_key=True, index=True)
#     item = Column(String, nullable=False)   # NEW: item name
#     amount = Column(Float, nullable=False)
#     date = Column(Date, nullable=False)
from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String, nullable=False)   # item name
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
