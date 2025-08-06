from graph import Graph
from test import test

@test
def dfs(start='A', target='J', alt=False):
    if start == target:
        return start
    graph = Graph(target=target, alt=alt)
    stack = [(start, None)]
    seen = set()
    seen_pairs = []
    iteration = 0

    while stack:
        iteration += 1
        curr_pair = stack.pop()
        N = curr_pair[0]

        if N in seen:
            continue

        seen.add(N)
        seen_pairs.append(curr_pair)

        if graph.goal(N):
            return graph.reconstruct(seen_pairs)

        n_nodes = graph.neighbors(N)
        n_nodes = graph.remove_seen(seen, n_nodes)
        n_pairs = graph.add_parent(n_nodes, N)
        stack.extend(n_pairs)

        if iteration > 100:
            return None


if __name__ == '__main__':
    dfs(start='A', target='V')
