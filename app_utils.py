import random
import string

def generate_ref(length=12):
    """Very basic mock external ref generator."""
    chars = string.ascii_uppercase + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def simulate_payment_gateway(amount: float, currency: str) -> bool:
    """Simulate a payment gateway (success 80%). For demo only; replace with real gateway."""
    return random.random() < 0.8