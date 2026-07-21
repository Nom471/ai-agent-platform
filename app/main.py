from fastapi import FastAPI

app = FastAPI(title= "AI Agent Platform")

@app.get("/")
def root():
    {"status": "online", "message": "AI Platform läuft"}