from typing import Any, Dict
from fastapi import FastAPI, Request, Response
from Score import Score
from dbConstant import getIsDebug

app = FastAPI()

@app.get("/")
def root():
    mode = "Local" if getIsDebug() else "Live"
    return f"Running {mode}"

@app.get("/{level}")
async def root(level:int,req:Request, res:Response):
    from dbAccessLayer import seeder
    return Score.getLevel(level)

@app.post("/")
async def store(data: Dict[str, Any],req:Request, res:Response):
    try:
        return Score.storeScore(data)
    except Exception as e:
        res.status_code = 404
        return e
