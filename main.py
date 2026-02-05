from fastapi import FastAPI, Request, Header, HTTPException
from pydantic import BaseModel
import time

app = FastAPI(title="Agentic Honeypot API")

API_KEY = "guvi-secret-123"  # you can change this

class HoneypotRequest(BaseModel):
    message: str | None = None

@app.get("/")
def health():
    return {"status": "alive"}

@app.post("/honeypot")
async def honeypot(
    request: Request,
    data: HoneypotRequest,
    x_api_key: str = Header(None)
):
    # Auth check
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    client_ip = request.client.host
    user_agent = request.headers.get("user-agent")

    time.sleep(1)

    log = {
        "ip": client_ip,
        "agent": user_agent,
        "message": data.message
    }

    print("HONEYPOT HIT:", log)

    return {
        "scam_detected": True,
        "extracted_entities": {
            "upi_id": "scammer@upi",
            "phone": "9876543210",
            "phishing_url": "http://fake-bank-login.com"
        },
        "confidence": 0.91
    }
