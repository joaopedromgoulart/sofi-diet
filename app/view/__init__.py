from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
async def home():
    data = {
        "text": "hi"
    }
    return {"data": data}
