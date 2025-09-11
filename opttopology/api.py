from fastapi import FastAPI,Depends
import os

app = FastAPI()


def call_sensor():
    return RuntimeError("'call_sensor' Not implemented")

def call_network():
    return RuntimeError("'call_network' Not implemented")

@app.get("/")
def read_root(net=Depends(call_network)):
    return {"msg": f"Hello from FastAPI!{net.sensors}"}


@app.post("/set_freq/")
def set_freq():
    return {"msg": "Hello from FastAPI!"}