# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from datetime import date
# from . import models, database
# from pydantic import BaseModel

# # Create tables
# models.Base.metadata.create_all(bind=database.engine)

# app = FastAPI()

# # Dependency
# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Pydantic schema
# class ExpenseCreate(BaseModel):
#     item: str
#     amount: float
#     date: date

# @app.post("/add_expense/")
# def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
#     db_expense = models.Expense(
#         item=expense.item,
#         amount=expense.amount,
#         date=expense.date
#     )
#     db.add(db_expense)
#     db.commit()
#     db.refresh(db_expense)
#     return {"message": "Expense added successfully", "expense": db_expense.id}

# @app.get("/expenses/")
# def get_expenses(db: Session = Depends(get_db)):
#     return db.query(models.Expense).all()

# @app.get("/daily_total/{day}")
# def daily_total(day: date, db: Session = Depends(get_db)):
#     total = db.query(models.Expense).filter(models.Expense.date == day).with_entities(
#         database.func.sum(models.Expense.amount)
#     ).scalar()
#     return {"date": str(day), "total": total or 0}

# @app.get("/monthly_total/{year}/{month}")
# def monthly_total(year: int, month: int, db: Session = Depends(get_db)):
#     total = db.query(models.Expense).filter(
#         database.func.strftime("%Y", models.Expense.date) == str(year),
#         database.func.strftime("%m", models.Expense.date) == f"{month:02d}"
#     ).with_entities(database.func.sum(models.Expense.amount)).scalar()
#     return {"year": year, "month": month, "total": total or 0}
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import date
from . import models, database
from pydantic import BaseModel

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema
class ExpenseCreate(BaseModel):
    item: str
    amount: float
    date: date

@app.post("/add_expense/")
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = models.Expense(
        item=expense.item,
        amount=expense.amount,
        date=expense.date
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return {"message": "Expense added successfully", "expense": db_expense.id}

@app.get("/expenses/")
def get_expenses(db: Session = Depends(get_db)):
    return db.query(models.Expense).all()

@app.get("/daily_total/{day}")
def daily_total(day: date, db: Session = Depends(get_db)):
    total = db.query(models.Expense).filter(models.Expense.date == day).with_entities(
        database.func.sum(models.Expense.amount)
    ).scalar()
    return {"date": str(day), "total": total or 0}

@app.get("/monthly_total/{year}/{month}")
def monthly_total(year: int, month: int, db: Session = Depends(get_db)):
    total = db.query(models.Expense).filter(
        database.func.strftime("%Y", models.Expense.date) == str(year),
        database.func.strftime("%m", models.Expense.date) == f"{month:02d}"
    ).with_entities(database.func.sum(models.Expense.amount)).scalar()
    return {"year": year, "month": month, "total": total or 0}
