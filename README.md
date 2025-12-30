# Secure Payment Gateway API

A security-focused REST API built with FastAPI. This project demonstrates backend engineering best practices, including credential protection, traffic auditing, and automated risk mitigation.

## Core Features

* **Identity Security**: Implements salted and hashed password storage using the Bcrypt algorithm with the Passlib library to protect user credentials.
* **Audit Logging Middleware**: Custom middleware layer that intercepts requests to provide security headers (X-Frame-Options, X-Content-Type-Options) and logs high-risk activities.
* **Fraud Detection Logic**: Built-in transaction monitoring that flags transfers exceeding specific risk thresholds (e.g., amounts over 5,000).
* **Data Validation**: Uses Pydantic schemas to enforce strict data integrity, including email format verification and positive-only currency constraints.

## Technical Stack

* **Framework**: FastAPI
* **Server**: Uvicorn
* **Security**: Passlib (Bcrypt), Python-Jose
* **Validation**: Pydantic, Email-Validator

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/k00p404/secure-payment-api.git](https://github.com/k00p404/secure-payment-api.git)
   cd secure-payment-api

2. **Initialize Virtual Environment**:
   python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. **Install Dependencies**:
pip install -r requirements.txt

4. **Run the Application**:
uvicorn app.main:app --reload --reload-dir app

## API Documentation

Once the server is running, you can access the interactive Swagger UI documentation at:
**http://127.0.0.1:8000/docs**

This interface allows you to test the **/register** and **/transfer** endpoints directly from the browser.

## Project Structure

* **app/main.py**: Application entry point and routing logic.
* **app/auth.py**: Security utilities and password hashing.
* **app/middleware.py**: Security headers and audit logging.
* **app/schemas.py**: Pydantic models for request/response validation.