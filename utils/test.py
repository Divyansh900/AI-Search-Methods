import time

def test(func):
    def new(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'\n{func.__name__.replace("_", " ").upper()}\nO/P:     {result}\nruntime: {end-start:.6f}ns\n')
        return result
    return new