from sympy.solvers.diophantine.diophantine import reconstruct

from graph import Graph
from test import test

@test
def bfs(start='A', target='D', alt=False):
    graph = Graph(target=target, alt=alt)

    queue = [(start, None)]
    seen = set()
    seen_pairs = []
    order = []

    iteration = 0

    while queue:
        iteration =+ 1
        curr_pair = queue.pop(0)
        N = curr_pair[0]

        if N in seen:
            continue
        order.append(N)
        seen.add(N)
        seen_pairs.append(curr_pair)

        if graph.goal(N):
            return graph.reconstruct(seen_pairs)

        n_nodes = graph.neighbors(N)
        n_nodes = graph.remove_seen(seen, n_nodes)
        n_pairs = graph.add_parent(n_nodes, N)

        queue.extend(n_pairs)

        if iteration > 100:
            return None


if __name__ == '__main__':
    bfs('A', 'V')