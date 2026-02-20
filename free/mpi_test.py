from mpi4py import MPI 
import time 
import numpy as np 


comm = MPI.COMM_WORLD
time_begin = time.time()

myrank = comm.Get_rank()
world_size = comm.Get_size()

length_data = 100

part_size = length_data // world_size 

i_start = myrank * part_size 
i_end = i_start + part_size 

if (myrank == (world_size - 1)):
    i_end = length_data

x = []
for i in range(i_start, i_end):
    x.append(i)

gathered_x = comm.gather(x, root=0)

if (myrank == 0):
    print(gathered_x)

time_end = time.time()
print(f"Total time taken = {time_end - time_begin}")