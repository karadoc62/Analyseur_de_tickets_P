from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_home():
    return {"message": "AI Ticket Lab"}


@app.get("/health")
def get_health():
    return {"status": "ok"}
    

