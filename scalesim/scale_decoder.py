import os
import argparse
from scalesim.scale_sim import scalesim


parser = argparse.ArgumentParser(description="Please provide config and model file paths")

parser.add_argument("-ts","--topologies",type=str,help="topologies folder path")
parser.add_argument("-c","--config",type=str,help="config file path")

# directory_path = '/home/jmalekar/Documents/scale-sim-v2/topologies/opt_models'
# directory_contents = os.listdir(directory_path)
# config='/home/jmalekar/Documents/scale-sim-v2/configs/google.cfg'

gemm_input = "gemm"

args=parser.parse_args()
topology_directory=args.topologies
config=args.config

topology_directory_contents=os.listdir(topology_directory)


print(topology_directory_contents)


for topology in topology_directory_contents:
        topology=topology_directory+"/"+topology
        logpath="../test_runs/"
        s = scalesim(save_disk_space=True, verbose=True,config=config,topology=topology,input_type_gemm=gemm_input)
        s.run_scale(top_path=logpath)