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


def custom_sort_key(filename):
    # Extract the first number from the filename
    first_number = int(filename.split('-')[0])
    
    # Extract the last number from the filename (before .csv)
    last_number = int(filename.split('_')[-1].split('.')[0])
    
    # Return a tuple for sorting
    return (first_number, last_number)

sorted_array = sorted(topology_directory_contents, key=custom_sort_key)


for topology in sorted_array:
        topology=topology_directory+"/"+topology
        logpath="../test_runs/"
        s = scalesim(save_disk_space=True, verbose=True,config=config,topology=topology,input_type_gemm=gemm_input)
        s.run_scale(top_path=logpath)