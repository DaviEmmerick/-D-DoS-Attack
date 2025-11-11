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

@app.get("/api/data")
@limiter.limit(TEN_PER_MINUTE) 
async def get_data_protected(request: Request):
    try:
        await asyncio.sleep(0.01) 
    except Exception as e:
        print(f"Erro no sleep: {e}")
        
    return {"message": "API (Protegida) está funcionando!"}

@app.exception_handler(RateLimitExceeded)
async def custom_rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):

    print(f"Rate limit excedido para {request.client.host}")
    return JSONResponse(
        status_code=429,
        content={"detail": f"Rate limit excedido: {exc.detail}"}
    )

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8002)

# run: uvicorn api-unprotected:app --port 8002