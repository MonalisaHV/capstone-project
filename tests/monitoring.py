import time
import logging

def monitor(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        logging.info(f"Execution time: {duration:.4f} seconds")
        return result
    return wrapper
