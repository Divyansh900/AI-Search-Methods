from utils.test import test
from utils.heuristic_graph import Graph

@test
def simulated_annealing(start:str, target:str, temperature:float|int=10.0):
    node = start
    b_node = start

    for i in range(10):
