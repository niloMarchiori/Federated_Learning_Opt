from topology.server.Opt_Model.sub1 import solve_SUB1

model_inputs= {"kappa": 10,
                "N": 1,
                "alpha": 2e-28,
                "num_samples":[6000, 10000, 15000, 12000, 8000, 4000],
                "D": [259700928, 519401856, 649277568, 649277568, 346301568, 173150784],
                "c": [9, 5, 4, 4, 8, 11],
                "fmin": [1300000000.0, 1300000000.0, 1300000000.0, 1300000000.0, 1300000000.0, 1300000000.0],
                "fmax": [2300000000, 2900000000, 2700000000, 2500000000, 2100000000, 2100000000]
                }
inputs={k: val if type(val) !=list else [] for k,val in model_inputs.items()}
print(inputs)


def run_opt_model(self=None, selected_trainers=None,model_inputs=None):
    if not selected_trainers:
        selected_trainers=self.get_trainer_list()

    if not model_inputs:
        model_inputs=self.model_inputs

    trainer_list=[f'sta{i}' for i in range(6)]
    select_inputs={k: val if type(val) !=list else [] for k,val in model_inputs.items()}
    for trainer in selected_trainers:
        trainer_idx=trainer_list.index(trainer)
        for key,val in model_inputs.items():
            if type(val)!=list:
                continue
            select_inputs[key].append(val[trainer_idx])
    select_inputs['N']=len(selected_trainers)
    
    T_cmp, f = solve_SUB1(**select_inputs)
    # self.save_input_model()
    frequency_dict = {}
    for key,val in zip(selected_trainers, f):
        frequency_dict[key] = val

    # Tcom, t,p = solve_SUB2(ctt.N, kappa=k, s=inp.s, B=inp.B, N0=inp.N0, h=inp.h, pmin=inp.pmin, pmax=inp.pmax)
    # thteta, eta = solve_SUB3(f, t, T_cmp, Tcom, k)
    return frequency_dict

print(run_opt_model(selected_trainers=['sta1','sta4'],model_inputs=model_inputs))