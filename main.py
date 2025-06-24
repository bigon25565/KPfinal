from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from datetime import datetime
import re

app = FastAPI()
LOGIN = "your_login_here"  # ← замените на ваш логин

@app.get("/{date_path}")
async def get_date(date_path: str):
    today = datetime.today()
    expected_path = today.strftime("%d%m%y")  # DDMMYY

    if date_path == expected_path:
        return JSONResponse(
            content={"date": today.strftime("%d-%m-%Y"), "login": LOGIN},
            media_type="application/json"
        )
    raise HTTPException(status_code=404, detail="Not found")

@app.get("/api/rv/{abc}")
async def reverse_string(abc: str):
    if re.fullmatch(r"[a-z]+", abc):
        return PlainTextResponse(abc[::-1], media_type="text/plain")
    raise HTTPException(status_code=400, detail="Invalid input: only lowercase letters allowed.")
