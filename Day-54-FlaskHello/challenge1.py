import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 


def speed_calc_decorator(function):
  def wrapper_function():
    start = time.time()
    function()
    finish = time.time()
    run_time = finish - start
    print(f"{function.__name__} run speed: {run_time:.3f}s")
  return wrapper_function


@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i   #type: ignore
        
@speed_calc_decorator
def slow_function():
  for i in range(100000000):
    i * i   #type: ignore


fast_function()
slow_function()