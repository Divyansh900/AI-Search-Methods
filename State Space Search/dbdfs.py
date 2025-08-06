from graph import Graph
from test import test
from dfs import dfs

@test
def dbdfs(start = 'A', target = 'D', depth_bound=3, alt = False):
    graph = Graph(target, alt)

    stack = [(start, None)]
    seen = set()
    seen_pairs = []

    depth = 0
    iteration = 0

    while stack:
        curr_pair = stack.pop(0) if depth == depth_bound else stack.pop()

        N = curr_pair[0]

        if N in seen:
            continue

        seen.add(N)
        seen_pairs.append(curr_pair)

        if graph.goal(N):
            return graph.reconstruct(seen_pairs)

        n_nodes = graph.remove_seen(seen ,graph.neighbors(N))
        n_pairs = graph.add_parent(n_nodes, N)

        stack.extend(n_pairs)
        depth += 1
        if iteration > 100:
            return None


if __name__ == '__main__':
    dbdfs('A', 'V', 2, )
    dfs('A', 'V', )


