from fastapi import FastAPI, Request
from pydantic import BaseModel
import time

app = FastAPI(title="Agentic Honeypot API")

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(data: LoginRequest, request: Request):
    client_ip = request.client.host
    user_agent = request.headers.get("user-agent")

    time.sleep(2)

    print("HONEYPOT HIT:", {
        "ip": client_ip,
        "username": data.username,
        "agent": user_agent
    })

    return {
        "status": "success",
        "token": "fake-jwt-token"
    }
