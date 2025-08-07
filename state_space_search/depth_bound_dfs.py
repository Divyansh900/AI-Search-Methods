from utils.graph import Graph
from utils.test import test
from depth_first_search import dfs


@test
def dbdfs(start='A', target='D', depth_bound=3, alt=False):
    graph = Graph(target, alt)

    stack = [(start, None, 0)]
    seen = set()
    seen_pairs = []

    iteration = 0
    while stack:
        N, parent, depth = stack.pop()

        if N in seen:
            continue

        if depth <= depth_bound:
            curr_pair = (N, parent)
            seen.add(N)
            seen_pairs.append(curr_pair)

            if graph.goal(N):
                return graph.reconstruct(seen_pairs)

            n_nodes = graph.remove_seen(seen, graph.neighbors(N))
            n_pairs = graph.add_parent(n_nodes, N, depth + 1)

            stack.extend(n_pairs)

        if iteration > 100:
            break

    return None


if __name__ == '__main__':
    dbdfs('A', 'V', 3)
    dfs('A', 'V')
