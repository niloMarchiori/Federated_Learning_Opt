from fastapi import FastAPI,Depends
import os
from pydantic import BaseModel

class Frequency(BaseModel):
    value: float

class Power(BaseModel):
    level: float 
    sensor: str 

def call_sensor():
    return RuntimeError("'call_sensor' Not implemented")

def call_network():
    return RuntimeError("'call_network' Not implemented")

def cmd_set_freq(value):
    os.system(f'sudo cpupower frequency-set -u {value}GHz; sudo cpupower frequency-set -d {value}GHz')

app = FastAPI()

@app.get("/")
def read_root(net=Depends(call_network)):
    return {"msg": "Hello from FastAPI!"}


@app.post("/set_cpufreq/")
def set_freq(freq: Frequency,clients=Depends(call_sensor)):
    value=freq.value
    cmd_set_freq(value)
    return {"msg": f"Frequency of cpus setted to {value}"}
    
    

@app.post("/set_power/")
def set_power(power: Power,net=Depends(call_network)):
    return {"msg": "Hello from FaastAPI!"}