from utils.test import test
from utils.heuristic_graph import Graph
import random as r

@test
def random_walk(start:str, target:str):
    graph = Graph(target)

    node = start
    path = [start]
    while not graph.goal(node):
        n_nodes = graph.neighbors(node)
        ind =  r.randint(0, len(n_nodes)-1)
        node = n_nodes[ind]
        path.append(node)

    return ' -> '.join(path)


if __name__ == '__main__':
    random_walk('A', 'B')