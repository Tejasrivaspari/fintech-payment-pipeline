from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentCreate(BaseModel):
    user_id: str
    amount: float
    currency: str = "USD"

class PaymentUpdate(BaseModel):
    status: str
    external_ref: Optional[str] = None

class PaymentOut(PaymentCreate):
    id: int
    status: str
    created_at: datetime
    external_ref: Optional[str] = None

    class Config:
        from_attributes = True