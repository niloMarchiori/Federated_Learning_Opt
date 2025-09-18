from federated.node import ClientSensor, ServerSensor


class SensorOpt(ClientSensor):
    def __init__(self,cores:int,cpu_freq:list[float,float],tx_power:list[int,int], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cores=cores
        self.cpu_freq=cpu_freq
        self.tx_power=tx_power
        

