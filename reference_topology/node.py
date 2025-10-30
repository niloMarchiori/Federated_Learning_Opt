from federated.node import ClientSensor, ServerSensor


class SensorOpt(ClientSensor):
    def __init__(self,cores:str,cpu_freq_curr:float,cpu_freq_min:float,cpu_freq_max:float,tx_power:None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cores=cores
        self.cpu_freq_curr=cpu_freq_curr
        self.cpu_freq_min=cpu_freq_min
        self.cpu_freq_max=cpu_freq_max
        self.tx_power=tx_power
        self.data_sz=0
        self.model_size=0

    
        

