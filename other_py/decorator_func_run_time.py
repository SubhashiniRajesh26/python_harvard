import functools
# from symbol import decorator
import time

def decorator_timer(func):
    """ Print the run time of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        run_time = end - start
        print(f"Finished in {run_time:.4f} secs")
        return value
    return wrapper_timer

@decorator_timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(500)])

waste_some_time(2)
