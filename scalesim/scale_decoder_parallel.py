import os
import argparse
from scalesim.scale_sim import scalesim
from mpi4py import MPI
import multiprocessing as mp

def custom_sort_key(filename):
    first_number = int(filename.split('-')[0])
    last_number = int(filename.split('_')[-1].split('.')[0])
    return (first_number, last_number)

def process_topology(topology, config, logpath, gemm_input):
    topology_path = os.path.join(topology_directory, topology)
    s = scalesim(save_disk_space=True, verbose=True, config=config, topology=topology_path, input_type_gemm=gemm_input)
    s.run_scale(top_path=logpath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Please provide config and model file paths")
    parser.add_argument("-ts", "--topologies", type=str, help="topologies folder path")
    parser.add_argument("-c", "--config", type=str, help="config file path")
    args = parser.parse_args()

    topology_directory = args.topologies
    config = args.config
    gemm_input = "gemm"
    logpath = "../test_runs/"

    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        # Master process
        topology_directory_contents = os.listdir(topology_directory)
        sorted_array = sorted(topology_directory_contents, key=custom_sort_key)
        
        # Distribute work among processes
        chunks = [sorted_array[i::size] for i in range(size)]
    else:
        chunks = None

    # Scatter chunks to all processes
    local_chunk = comm.scatter(chunks, root=0)

    # Set up multiprocessing Pool
    num_cores = mp.cpu_count()
    pool = mp.Pool(processes=num_cores)

    # Process local chunk using multiprocessing
    pool.starmap(process_topology, [(topology, config, logpath, gemm_input) for topology in local_chunk])

    pool.close()
    pool.join()

    # Wait for all processes to finish
    comm.Barrier()
