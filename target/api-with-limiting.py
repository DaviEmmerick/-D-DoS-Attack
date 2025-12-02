from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import uvicorn
import asyncio

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

TEN_PER_MINUTE = "10/minute"
ip_counts = {}      # Conta quantas vezes o IP bateu no servidor
banned_ips = set()  # Lista de IPs bloqueados
BLOCK_LIMIT = 50

@app.get("/api/data")
@limiter.limit(TEN_PER_MINUTE) 
async def get_data_protected(request: Request):
    client_ip = request.client.host

    if client_ip in banned_ips:
        return JSONResponse(status_code=403, content={"detail": "IP BANIDO PERMANENTEMENTE."})
    
    ip_counts[client_ip] = ip_counts.get(client_ip, 0) + 1

    if ip_counts[client_ip] > BLOCK_LIMIT:
        banned_ips.add(client_ip)
        return JSONResponse(status_code=403, content={"detail": "Limite de segurança excedido. IP Banido."})
        
    return {"message": "API (Protegida) está funcionando!"}

@app.exception_handler(RateLimitExceeded)
async def custom_rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    client_ip = request.client.host

    if client_ip in banned_ips:
        return JSONResponse(status_code=403, content={"detail": "IP BANIDO PERMANENTEMENTE."})

    ip_counts[client_ip] = ip_counts.get(client_ip, 0) + 1

    if ip_counts[client_ip] > BLOCK_LIMIT:
        banned_ips.add(client_ip)
        print(f"[FIREWALL] IP {client_ip} banido por insistência no Rate Limit.")
        return JSONResponse(status_code=403, content={"detail": "Limite de segurança excedido. IP Banido."})

    print(f"Rate limit excedido para {request.client.host}")
    return JSONResponse(
        status_code=429,
        content={"detail": f"Rate limit excedido: {exc.detail}"}
    )

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8002)

# run: uvicorn api-with-limiting:app --port 8002