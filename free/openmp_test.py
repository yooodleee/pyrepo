import time 
from joblib import Parallel, delayed 


time_begin = time.time()
length_data = 100

x = []

def function_loop(i):
    return (i)

n_cores = 2
openMP_result = Parallel(n_jobs=int(n_cores))(delayed(function_loop)(i) for i in range(length_data))
print(openMP_result)

time_end = time.time()

print(f"Total time taken = {time_end - time_begin}")