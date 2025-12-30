from fastapi import FastAPI, status
from .schemas import Transaction, UserCreate
from .auth import get_password_hash
from .middleware import SecurityAuditMiddleware

# Initialize the FastAPI application instance
app = FastAPI(title="Secure FinTech Gateway")

# Register custom middleware for automated security headers and audit logging
app.add_middleware(SecurityAuditMiddleware)

# Volatile in-memory store representing a user database
users_db = {}

@app.get("/")
def health_check():
    # Service availability endpoint to monitor API status
    return {"status": "Online", "version": "1.0.0"}

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    # Handles user onboarding
    # Passwords are processed via a one-way hashing function (Bcrypt) before storage
    hashed_password = get_password_hash(user.password)
    users_db[user.username] = {"username": user.username, "password": hashed_password}
    return {"message": "User registered successfully"}

@app.post("/transfer")
async def process_transfer(transaction: Transaction):
    # Main transaction logic
    # Implements a baseline risk-assessment threshold to flag high-value transactions
    if transaction.amount > 5000:
        return {
            "status": "Flagged", 
            "message": "Transaction exceeds risk threshold."
        }
    return {"status": "Approved", "details": transaction}