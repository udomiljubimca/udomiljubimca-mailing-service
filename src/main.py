import uvicorn
from fastapi import FastAPI, HTTPException
from send_email import EmailToSend
from pydantic import BaseModel

app = FastAPI()
class itemEmail(BaseModel):
    email: str
    title: str
    message: str
@app.post("/send-email")
async def send_email(item: itemEmail):
    check = EmailToSend(item.email, item.message, item.title).send()
    if check['email_sended'] == True:
        EmailToSend(item.email, item.message, item.title).send()
    else:
        raise HTTPException(status_code = 500, detail = "Something went wrong") 
    return {"message" : "email sent successfully"}
 
@app.get("/health")
async def index():
    return {"HEALTH" : "OK"}
 
if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")