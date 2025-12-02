from fastapi import FastAPI
import uvicorn
import asyncio 

app = FastAPI()

@app.get("/api/data")
async def get_data():
    try:
        await asyncio.sleep(2.0) 
    except Exception as e:
        print(f"Erro no sleep: {e}")
        
    return {"message": "API (Desprotegida) está funcionando!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

# run: uvicorn api-unprotected:app --port 8001