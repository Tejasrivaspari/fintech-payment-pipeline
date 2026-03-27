from sqlalchemy.orm import Session
from app import models, schemas
from app.utils import generate_ref, simulate_payment_gateway

def create_payment(db: Session, payment: schemas.PaymentCreate) -> models.Payment:
    external_ref = generate_ref()
    success = simulate_payment_gateway(payment.amount, payment.currency)
    status = "succeeded" if success else "failed"

    db_payment = models.Payment(
        user_id=payment.user_id,
        amount=payment.amount,
        currency=payment.currency,
        status=status,
        external_ref=external_ref,
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_payment(db: Session, payment_id: int) -> models.Payment:
    return db.query(models.Payment).filter(models.Payment.id == payment_id).first()

def list_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Payment).offset(skip).limit(limit).all()