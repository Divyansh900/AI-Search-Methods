import time

def test(func):
    def new(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__.upper()}\nO/P:{result}\nruntime:{end-start}ns\n')
        return result
    return new