from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app import models, schemas, services
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FinTech Payment Pipeline (Demo)")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "FinTech Payment Pipeline API (Demo)"}

@app.post("/payments", response_model=schemas.PaymentOut)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    db_payment = services.create_payment(db, payment)
    return db_payment

@app.get("/payments/{payment_id}", response_model=schemas.PaymentOut)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = services.get_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@app.get("/payments", response_model=list[schemas.PaymentOut])
def read_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payments = services.list_payments(db, skip=skip, limit=limit)
    return payments