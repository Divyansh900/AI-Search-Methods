import math


class Graph:
    def __init__(self, target, alt=False):
        """
        Initialize graph with adjacency list and coordinates for heuristic calculations.

        Args:
            alt (bool): If True, use small test graph. If False, use larger graph.
        """
        self.alt = alt
        self.target = target

        if alt:
            self._init_small_graph()
        else:
            self._init_large_graph()

    def _init_small_graph(self):
        # Small test graph (6 nodes)
        self.adjacency_list = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }

        # Coordinates for heuristic calculations (x, y)
        self.coordinates = {
            'A': (0, 0),
            'B': (1, 0),
            'C': (0, 1),
            'D': (2, 0),
            'E': (1, 1),
            'F': (0, 2)
        }

        # Target nodes for heuristic
        self.target_nodes = {'D', 'F'}

    def _init_large_graph(self):
        # Larger graph (26 nodes, A-Z)
        self.adjacency_list = {
            'A': ['B', 'C', 'E'],
            'B': ['A', 'D', 'F'],
            'C': ['A', 'G', 'H'],
            'D': ['B', 'I', 'J'],
            'E': ['A', 'K', 'L'],
            'F': ['B', 'M', 'N'],
            'G': ['C', 'O', 'P'],
            'H': ['C', 'Q'],
            'I': ['D', 'R'],
            'J': ['D', 'S', 'T'],
            'K': ['E', 'U'],
            'L': ['E', 'V'],
            'M': ['F', 'W'],
            'N': ['F', 'X'],
            'O': ['G', 'Y'],
            'P': ['G', 'Z'],
            'Q': ['H', 'R'],
            'R': ['I', 'Q', 'S'],
            'S': ['J', 'R', 'T'],
            'T': ['J', 'S', 'U'],
            'U': ['K', 'T', 'V'],
            'V': ['L', 'U', 'W'],
            'W': ['M', 'V', 'X'],
            'X': ['N', 'W', 'Y'],
            'Y': ['O', 'X', 'Z'],
            'Z': ['P', 'Y']
        }

        # Coordinates for heuristic calculations (arranged in a 6x5 grid roughly)
        self.coordinates = {
            'A': (0, 0), 'B': (1, 0), 'C': (2, 0), 'D': (3, 0), 'E': (4, 0),
            'F': (0, 1), 'G': (1, 1), 'H': (2, 1), 'I': (3, 1), 'J': (4, 1),
            'K': (0, 2), 'L': (1, 2), 'M': (2, 2), 'N': (3, 2), 'O': (4, 2),
            'P': (0, 3), 'Q': (1, 3), 'R': (2, 3), 'S': (3, 3), 'T': (4, 3),
            'U': (0, 4), 'V': (1, 4), 'W': (2, 4), 'X': (3, 4), 'Y': (4, 4),
            'Z': (2, 5)
        }

        # Target nodes for heuristic
        self.target_nodes = {'T', 'X', 'Z'}

    def neighbors(self, node):
        """
        Get neighbors of a given node.

        Args:
            node: The node to get neighbors for

        Returns:
            List of neighbor nodes
        """
        return self.adjacency_list.get(node, [])

    def goal(self, node: str):
        return node == self.target

    def reconstruct(self, nodes, target:str|None = None):
        t = target if target else self.target
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

    def argmin_score(self, nodes):
        ind = -1
        for n in range(len(nodes)):
            if self.heuristic_score(nodes[n]) < self.heuristic_score(nodes[ind]):
                ind = n

        return ind

    def diff_score(self, a, b):
        return self.heuristic_score(a) - self.heuristic_score(b)

    def remove_seen(self, seen_list, neighbors):
        return [i for i in neighbors if i not in seen_list]

    def add_parent(self, nodes: list, parent: str, score_type: str = 'manhattan'):
        return [(n, parent, self.heuristic_score(n, score_type)) for n in nodes]

    def get_nodes(self):
        """Get all nodes in the graph."""
        return list(self.adjacency_list.keys())

    def has_node(self, node):
        """Check if node exists in graph."""
        return node in self.adjacency_list

    def has_edge(self, node1, node2):
        """Check if edge exists between two nodes."""
        return (node1 in self.adjacency_list and
                node2 in self.adjacency_list[node1])

    def get_coordinates(self, node):
        """Get coordinates of a node."""
        return self.coordinates.get(node)

    def manhattan_distance(self, node1, node2='Z'):
        """
        Calculate Manhattan distance between two nodes.

        Args:
            node1, node2: Nodes to calculate distance between

        Returns:
            Manhattan distance as float
        """
        if node1 not in self.coordinates or node2 not in self.coordinates:
            return float('inf')

        x1, y1 = self.coordinates[node1]
        x2, y2 = self.coordinates[node2]
        return abs(x1 - x2) + abs(y1 - y2)

    def euclidean_distance(self, node1, node2='Z'):
        """
        Calculate Euclidean distance between two nodes.

        Args:
            node1, node2: Nodes to calculate distance between

        Returns:
            Euclidean distance as float
        """
        if node1 not in self.coordinates or node2 not in self.coordinates:
            return float('inf')

        x1, y1 = self.coordinates[node1]
        x2, y2 = self.coordinates[node2]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def heuristic_score(self, node, distance_type='manhattan'):
        """
        Calculate heuristic score for a node based on distance to closest target.

        Args:
            node: Node to calculate heuristic for
            distance_type: 'manhattan' or 'euclidean'

        Returns:
            Minimum distance to any target node
        """
        if not self.target or node not in self.coordinates:
            return 0

        distances = []

        if distance_type == 'euclidean':
            dist = self.euclidean_distance(node, self.target)
        else:  # default to manhattan
            dist = self.manhattan_distance(node, self.target)
        distances.append(dist)

        return min(distances)

    def display_graph_info(self):
        """Display basic information about the graph."""
        graph_type = "Small test graph" if self.alt else "Large graph"
        print(f"{graph_type}")
        print(f"Nodes: {len(self.adjacency_list)}")
        print(f"Target nodes: {self.target_nodes}")
        print(f"Sample neighbors - Node 'A': {self.neighbors('A')}")

        # Show heuristic scores for a few nodes
        sample_nodes = list(self.adjacency_list.keys())[:3]
        print("\nSample heuristic scores:")
        for node in sample_nodes:
            manhattan_h = self.heuristic_score(node, 'manhattan')
            euclidean_h = self.heuristic_score(node, 'euclidean')
            print(f"  {node}: Manhattan = {manhattan_h:.2f}, Euclidean = {euclidean_h:.2f}")


# Example usage:
if __name__ == "__main__":
    # Test with large graph
    print("=== Large Graph ===")
    large_graph = Graph(target='A', alt=False)
    large_graph.display_graph_info()

    print(f"\nNeighbors of 'M': {large_graph.neighbors('M')}")
    print(f"Heuristic score for 'A' (Manhattan): {large_graph.heuristic_score('A', 'manhattan'):.2f}")
    print(f"Heuristic score for 'A' (Euclidean): {large_graph.heuristic_score('A', 'euclidean'):.2f}")

    print("\n" + "=" * 40)

    # Test with small graph
    print("=== Small Graph ===")
    small_graph = Graph(target='A', alt=True)
    small_graph.display_graph_info()

    print(f"\nNeighbors of 'B': {small_graph.neighbors('B')}")
    print(f"Heuristic score for 'A' (Manhattan): {small_graph.heuristic_score('A', 'manhattan'):.2f}")
    print(f"Heuristic score for 'A' (Euclidean): {small_graph.heuristic_score('A', 'euclidean'):.2f}")
