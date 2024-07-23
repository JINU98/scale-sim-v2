import os
from scalesim.scale_sim import scalesim
directory_path = '/home/jmalekar/Documents/scale-sim-v2/topologies/opt_models'
directory_contents = os.listdir(directory_path)
config='/home/jmalekar/Documents/scale-sim-v2/configs/google.cfg'
gemm_input = "gemm"

for i in directory_contents:
    topology='/home/jmalekar/Documents/scale-sim-v2/topologies/opt_models/'+i
    logpath="../test_runs/"+i
    s = scalesim(save_disk_space=True, verbose=True,config=config,topology=topology,input_type_gemm=gemm_input)
    s.run_scale(top_path=logpath)