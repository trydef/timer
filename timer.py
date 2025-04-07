import time
import logging
from functools import wraps


logging.basicConfig(
    filename='execution.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def execution_timer(func):
    """Декоратор для логування часу виконання функції"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end = time.perf_counter()
            duration = end - start
            logging.info(f"Function '{func.__name__}' executed in {duration:.6f} seconds")
            print(f"Function '{func.__name__}' executed in {duration:.6f} seconds")
    return wrapper


@execution_timer
def example(delay=0.2):
    time.sleep(delay)
    return "done"