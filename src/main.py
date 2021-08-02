import uvicorn
from fastapi import FastAPI

app = FastAPI()
@app.get("/health")
async def index():
    return {"HEALTH" : "OK"}
 

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")