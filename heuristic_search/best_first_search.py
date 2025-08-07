from utils.heuristic_graph import Graph
from utils.test import test

@test
def best_first_search(start:str, target:str, alt:bool=False):
    graph = Graph(target, alt)

    stack = [(start, None, float('inf'))]
    seen = set()
    seen_pairs = []

    iteration = 0

    while stack:
        ind = -1
        N, parent, score = stack.pop()

        if N in seen:
            continue

        seen.add(N)
        seen_pairs.append((N, parent))

        if graph.goal(N):
            return graph.reconstruct(seen_pairs)

        n_nodes = graph.remove_seen(seen, graph.neighbors(N))
        n_pairs = graph.add_parent(n_nodes, N)
        stack.extend(n_pairs)
        for i in range(len(stack)):
            if stack[i][-1] > stack[ind][-1]:
                ind = i

        stack.append(stack.pop(0))

        if iteration>1000:
            return None


if __name__ == '__main__':
    best_first_search(start='A', target='X')