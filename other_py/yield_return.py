
from datetime import datetime
import tracemalloc
# import os
# from psutil import Process
# from memory_profiler import profile
# import memory_profiler

print("The output of tracemalloc is given in form of (current, peak),i.e, current memory is the memory the code is currently using and peak memory is the maximum space the program used while executing.")
start = datetime.now()
def yeild_demo():
    with open("/home/local/ZOHOCORP/subha-15406/python practice/sample-2mb-text-file.txt", "r") as f:
        lines = f.readline()
        yield lines
end = datetime.now()
time_taken = end - start
print('Time: ',time_taken) 
tracemalloc.start()


yeild_demo()
print(tracemalloc.get_traced_memory())

tracemalloc.stop()
        
start = datetime.now()
def return_demo():
     with open("/home/local/ZOHOCORP/subha-15406/python practice/sample-2mb-text-file.txt", "r") as f:
        lines = f.readline()
        return lines
end = datetime.now()
time_taken = end - start
print('Time: ',time_taken) 

tracemalloc.start()


return_demo()
print(tracemalloc.get_traced_memory())

tracemalloc.stop()

