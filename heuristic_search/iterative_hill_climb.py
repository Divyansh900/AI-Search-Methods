from utils.test import test
from utils.heuristic_graph import Graph

@test
def iterative_hill_climb(start: str, target: str, alt: bool = False):
    graph = Graph(target, alt)

    nodes = graph.get_nodes()
    nodes.insert(0, start)
    best_score = graph.heuristic_score(start, 'euclidean')
    best_seen = []
    tries = 0
    for node in nodes:
        neighbors = graph.neighbors(node)
        n_node = neighbors[graph.argmin_score(neighbors)]
        seen_pairs = [(node, None)]
        iteration = 0
        while graph.heuristic_score(n_node) < graph.heuristic_score(node):

            # BASICALLY THE HILL CLIMBING ALGORITHM
            seen_pairs.append((n_node, node))
            node = n_node

            neighbors = graph.neighbors(node)
            n_node = neighbors[graph.argmin_score(neighbors)]
            if iteration > 100:
                return 'exceed limit'
            iteration += 1

        dist = graph.heuristic_score(node, "euclidean")

        if dist < best_score:
            best_seen = seen_pairs

        if dist == 0:
            break
        tries +=1
    extra = f'    tried {tries} nodes' if tries != 0 else ''

    return graph.reconstruct(best_seen) + extra


if __name__ == '__main__':
    iterative_hill_climb('A', 'Z')