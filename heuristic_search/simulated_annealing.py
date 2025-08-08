from utils.test import test
from utils.heuristic_graph import Graph
import random
import numpy as np

def softmax(x):
    return 1 / (1 - np.exp(-x))

def score(diff, temp):
    if diff <= 0:
        return 1.0
    return np.exp(-diff/temp)

def diff_score(graph,a,b):
    graph.heuristic_score(a) - graph.heuristic_score(b)

@test
def simulated_annealing(start:str, target:str, epochs:int = 10, temperature:float|int=10.0, cooling_rate:float=0.25):

    graph = Graph(target)

    node = start
    b_node = start
    path = [start]
    for i in range(epochs):
        n_nodes = graph.neighbors(node)
        ind = random.randint(0, len(n_nodes)-1)
        n_node = n_nodes[ind]


        diff = graph.diff_score(n_node, node) # added small constant to prevent zero division error
        if random.random() < score(diff,temperature):

            node = n_node
            path.append(node)
            if graph.diff_score(node, b_node) > 0:
                b_node = node
        if node == target:
            break

        if temperature < 0.1:
            temperature = 0.1
        else:
            temperature = (1 - cooling_rate) * temperature

    extra = f'   Best node : {b_node}' if b_node != start else ''
    return '->'.join(path) + extra


if __name__ == "__main__":
    simulated_annealing('A', 'K', epochs=100, temperature=50, cooling_rate=0.1)