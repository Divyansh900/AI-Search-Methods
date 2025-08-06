class Graph:
    def __init__(self, target: str = 'H', alt=False):
        if alt:
            self.graph = {
                'A': ['C', 'D'],
                'B': ['C', 'E'],
                'C': ['A', 'B', 'D', 'E'],
                'D': ['A', 'C'],
                'E': ['B', 'C']
            }
        else:
            self.graph = {
                'A': ['B', 'H', 'M', 'Q', 'S', 'T', 'W', 'X'],
                'B': ['A', 'F', 'K', 'N'],
                'C': ['D', 'G', 'I', 'L', 'O', 'P', 'R', 'U', 'V', 'Y', 'Z'],
                'D': ['C', 'E', 'J', 'M', 'R', 'W'],
                'E': ['D', 'F', 'H', 'L', 'P', 'Q', 'S', 'U', 'V', 'X', 'Y'],
                'F': ['B', 'E', 'G', 'I', 'Z'],
                'G': ['C', 'F', 'H', 'K', 'N', 'T', 'Y'],
                'H': ['A', 'E', 'G', 'J', 'O', 'R'],
                'I': ['C', 'F', 'L', 'M', 'N', 'Q', 'T', 'U', 'W'],
                'J': ['D', 'H', 'K', 'P', 'S'],
                'K': ['B', 'G', 'J', 'L', 'O', 'V', 'X', 'Z'],
                'L': ['C', 'E', 'I', 'K', 'M', 'Q', 'R', 'T', 'Y', 'Z'],
                'M': ['A', 'D', 'I', 'L', 'N', 'P', 'U', 'W', 'X'],
                'N': ['B', 'G', 'I', 'M', 'O'],
                'O': ['C', 'H', 'K', 'N', 'Q', 'V', 'W', 'Y', 'Z'],
                'P': ['C', 'E', 'J', 'M', 'R', 'S', 'T'],
                'Q': ['A', 'E', 'I', 'L', 'O', 'U', 'V'],
                'R': ['C', 'D', 'H', 'L', 'P'],
                'S': ['A', 'E', 'J', 'P', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
                'T': ['A', 'G', 'I', 'L', 'P', 'S'],
                'U': ['C', 'E', 'I', 'M', 'Q', 'S', 'V'],
                'V': ['C', 'E', 'K', 'O', 'Q', 'S', 'U'],
                'W': ['A', 'D', 'I', 'M', 'O', 'S', 'X'],
                'X': ['A', 'E', 'K', 'M', 'S', 'W', 'Y'],
                'Y': ['C', 'E', 'G', 'L', 'O', 'S', 'X', 'Z'],
                'Z': ['C', 'F', 'K', 'L', 'O', 'S', 'Y']
            }
        self.target = target

    def neighbors(self, node: str):
        if node in self.graph.keys():
            return self.graph[node]
        else:
            raise KeyError(f'Invalid Node {node}')

    def goal(self, node: str):
        return node == self.target

    def __len__(self):
        return 26

    def reconstruct(self, nodes):
        t = self.target
        node_parent = {n: p for n, p in nodes}

        path = [t]
        c = t
        while c in node_parent and node_parent[c] is not None:
            temp = node_parent[c]
            path.append(temp)
            c = temp

        path.reverse()
        path = ' -> '.join(path)
        return path

    def remove_seen(self, seen: set, nodes):
        return [node for node in nodes if node not in seen]

    def add_parent(self, nodes: list, parent):
        return [(i, parent) for i in nodes]
