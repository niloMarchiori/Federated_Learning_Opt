from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello from FastAPI!"}

@app.post("/set_freq/")
def set_freq():
    return {"msg": "Hello from FastAPI!"}