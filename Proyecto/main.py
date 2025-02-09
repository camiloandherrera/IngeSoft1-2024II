# Hello world from the dev team!
from fastapi import FastAPI

app = FastAPI(title="ProjecTrack")

@app.get("/")
async def hello_root():
    return {
        "message": "Hello World",
        "signs": "The ProjectTrack dev team"
    }