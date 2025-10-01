from fastapi import FastAPI,Depends
import os
from pydantic import BaseModel

class Frequency(BaseModel):
    value: float
    trainer_id: str

class Power(BaseModel):
    level: float 
    sensor: str 

def call_sensor():
    return RuntimeError("'call_sensor' Not implemented")

def call_network():
    return RuntimeError("'call_network' Not implemented")

def cmd_set_freq(value,core):
    for i in core:
        os.system(f'sudo cpupower -c {i} frequency-set -u {value*1.01}GHz; sudo cpupower -c {i} frequency-set -d {value}GHz')

app = FastAPI()

@app.get("/")
def read_root(net=Depends(call_network)):
    return {"msg": "Hello from FastAPI!"}


@app.post("/set_cpufreq/")
def set_freq(freq: Frequency,clients=Depends(call_sensor)):
    value=freq.value
    trainer_id=freq.trainer_id
    for client in clients:
        if str(client.name) == trainer_id:
            cpus=client.resources['cpuset_cpus']
            cpus=cpus.split(',')
            cmd_set_freq(value,cpus)
            return {"msg": f"Frequency of cpus {cpus} setted to {value}"}
    
    return {"msg": "Erro ao setar frequencia, cliente nao encontrado"}

@app.post("/set_power/")
def set_power(power: Power,net=Depends(call_network)):
    return {"msg": "Hello from FaastAPI!"}