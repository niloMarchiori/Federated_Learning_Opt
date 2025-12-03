from topology import topology


def main():
    NUM_ROUNDS=1
    NUM_CLIENTS=6
    model_inputs= {"kappa": 100,
                "N": NUM_CLIENTS,
                "alpha": 2e-28,
                "num_samples":[10000,12000,13000,16000,18000,16000],
                "D": [284972440704, 397891747968, 461402112000, 602612083840, 602612083840, 602612083840],
                "c": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                "fmin": [1300000000.0, 1300000000.0, 1300000000.0, 1300000000.0, 1300000000.0, 1300000000.0],
                "fmax": [2374540118.8473625, 2950714306.4099164, 2731993941.811405, 2598658484.1970367, 2156018640.442436, 2155994520.3362026]
                }
    #Roda o experimento para D_n diferentes mas todas as classes

    server_args = {"min_trainers": NUM_CLIENTS, 
                   "num_rounds": NUM_ROUNDS,
                   "stop_acc": 0.999, 
                   'client_selector': 'All', 
                   'aggregator': "FedAvg", 
                   "model_inputs": model_inputs}

    client_args = {"mode": 'all same_samples','num_samples':15000,"trainer_class": "TrainerMNIST"}
    experiment_name = 'all_same_samples'

    client_script="flw/topology/client/client.py"
    
    #Corresponde as saidas com valores otimizados
    server_script="flw/topology/server/server_opt.py"
    topology(server_script,
             client_script, 
             server_args,
             client_args,
             model_inputs,
             cpu_governor='userspace',
             experiment_name=experiment_name,
             n_rounds=NUM_ROUNDS)

    #Corresponde as saidas com valores NAO otimizados
    server_script="flw/topology/server/server_ref.py"
    topology(server_script,
             client_script, 
             server_args,
             client_args,
             model_inputs,
             cpu_governor='ondemand',
             experiment_name=experiment_name,
             n_rounds=NUM_ROUNDS)

if __name__=='__main__':
    main()