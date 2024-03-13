import time
from dataclasses import dataclass


@dataclass
class TestClass:
    a: int = 1
    b: str = "B"


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result

    return wrapper


@timeit
def my_function(sec):
    p = TestClass()
    print(p)
    help(p)


if __name__ == "__main__":
    my_function(2)
