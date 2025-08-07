from utils.test import test
from utils.heuristic_graph import Graph

@test
def hill_climbing(start:str, target:str, alt:bool=False):
    graph = Graph(target=target, alt = alt)

    node = start
    neighbors = graph.neighbors(node)
    n_node = neighbors[graph.argmin_score(neighbors)]
    seen_pairs = [(node, None)]
    iteration = 0
    while graph.heuristic_score(n_node) < graph.heuristic_score(node):
        seen_pairs.append((n_node, node))
        node = n_node

        neighbors = graph.neighbors(node)
        n_node = neighbors[graph.argmin_score(neighbors)]
        if iteration>100:
            return 'exceed limit'
        iteration += 1

    dist = graph.heuristic_score(node, "euclidean")

    extra = f'   (dist to {target} : {dist:.3f})' if dist !=0 else ' '
    return graph.reconstruct(seen_pairs, target = node) + extra

if __name__ == "__main__":
    hill_climbing("A", 'L')