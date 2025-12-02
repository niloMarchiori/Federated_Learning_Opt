from topology import topology

NUM_ROUNDS=2

server_args = {"min_trainers": 6, "num_rounds": NUM_ROUNDS,
                    "stop_acc": 0.999, 'client_selector': 'All', 'aggregator': "FedAvg"}
client_args = {"mode": 'random r_samples', "trainer_class": "TrainerMNIST"}
experiment_name = 'r_samples'

def main():
    
    client_script="flw/topology/client/client.py"
    server_script="flw/topology/server/server_opt.py"
    topology(server_script,client_script)

    server_script="flw/topology/server/server_ref.py"
    topology(server_script,client_script)



if __name__ == '__main__':
    main()
