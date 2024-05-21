import time
from dataclasses import dataclass

from pandas_datareader import data as wb


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


# Dann musst du angeben, welchen Aktienindex du verwenden möchtest:


@timeit
def boerse():
    ticker_name = "^GSPC"
    # ^GSPC steht für S&P500, siehe https://finance.yahoo.com/quote/%5EGSPC/
    ticker = wb.DataReader(ticker_name, start="2010-1-1", data_source="yahoo")
    print(ticker)


if __name__ == "__main__":
    # my_function(2)
    boerse()
