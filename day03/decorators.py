import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"This took {end_time - start_time:.1f} seconds to complete.")
        return result
    return wrapper

@timer
def greet(name):
    for i in range(100000000):
        result = 3 + 4 ** 2
    return f"Hello {name}!"

print(greet("Grant"))
