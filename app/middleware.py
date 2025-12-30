import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Standard security logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SecurityAudit")

class SecurityAuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 1. Start timer to monitor performance/latency
        start_time = time.time()
        client_ip = request.client.host
        
        # 2. FRAUD DETECTION: Log high-risk endpoint access
        if request.method == "POST" and "/transfer" in request.url.path:
            logger.info(f"SECURITY ALERT: Transaction attempt detected from IP: {client_ip}")

        # 3. Process the request
        response = await call_next(request)
        
        # 4. ENFORCE SECURITY HEADERS: Prevent XSS and Clickjacking
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        
        return response