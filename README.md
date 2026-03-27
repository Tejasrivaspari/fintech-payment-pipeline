# fintech-payment-pipeline
# FinTech Payment Pipeline (Demo)

This is a **demo / mock payment pipeline** using FastAPI and SQLite.  
Payment processing is simulated (not connected to any real bank or gateway).

## Features

- Create payments with simulated gateway response
- Track payment status (pending, succeeded, failed)
- List all payments
- REST API via FastAPI

## Quick Start

```bash
pip install -r requirements.txt

uvicorn app.main:app --reload
```

API docs will be at `http://localhost:8000/docs`.

## Endpoints

- `POST /payments` – Create a payment
- `GET /payments/{id}` – Get a payment by ID
- `GET /payments` – List payments
