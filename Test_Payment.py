from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from app import models
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_payments.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[Depends(get_db)] = override_get_db

client = TestClient(app)

def test_create_payment():
    response = client.post(
        "/payments",
        json={"user_id": "u123", "amount": 100.0, "currency": "USD"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "u123"
    assert data["amount"] == 100.0
    assert data["status"] in ["succeeded", "failed"]