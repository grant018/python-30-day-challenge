import random

def retry(func):
    def wrapper(*args, **kwargs):
        for attempt in range(1, 4):
            try:
                result = func(*args, **kwargs)
                print(f"Attempt {attempt}: Success!")
                return result
            except Exception as e:
                print(f"Attempt {attempt} failed: {e}")
        return "All attempts failed."
    return wrapper
            
@retry
def coin_flip():
    if random.random() < 0.7:
        raise ValueError("Bad flip!")
    return "Success!"

print(coin_flip())
# Might print:
# Attempt 1 failed: Bad flip!
# Attempt 2 failed: Bad flip!
# Attempt 3: Success!