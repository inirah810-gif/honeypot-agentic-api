from fastapi import FastAPI, Header
from typing import Optional

app = FastAPI(title="Agentic Honeypot API")

@app.get("/")
def root():
    return {"status": "alive"}

@app.post("/honeypot")
def honeypot(
    x_api_key: Optional[str] = Header(None)
):
    if x_api_key != "guvi-secret-123":
        return {
            "status": "error",
            "message": "Invalid API key"
        }

    return {
        "status": "success",
        "honeypot": "active",
        "extracted_intel": {
            "upi_ids": ["scammer@upi"],
            "phone_numbers": ["+91XXXXXXXXXX"],
            "links": ["http://fake-link.com"]
        }
    }

    
