# State Space Search Algorithms
## Work in Progress
State space search algorithms explore a problem's solution space systematically to find a path from an initial state to a goal state. These are fundamental algorithms in artificial intelligence and computer science.

## 📚 Overview

State space search represents problems as:
- **States**: Configurations of the problem
- **Actions**: Transitions between states
- **Goal Test**: Condition to identify solution states
- **Path Cost**: Measure of solution quality

## 🔍 Algorithms Implemented

### 1. Depth First Search (DFS)

**Algorithm**: Explores as far as possible along each branch before backtracking.

```python
from state_space_search.depth_first_search import dfs

# Basic usage
result = dfs(start='A', target='J')
print(result)  # Output: A -> B -> F -> Z -> ... -> J

# Using alternative graph
result = dfs(start='A', target='E', alt=True)
```

**Characteristics**:
- **Time Complexity**: O(b^m) where b is branching factor, m is maximum depth
- **Space Complexity**: O(bm) - linear space
- **Complete**: No (can get stuck in infinite paths)
- **Optimal**: No (doesn't guarantee shortest path)

**Advantages**:
- Memory efficient
- Finds solution quickly if it exists along the first explored path
- Simple implementation

**Disadvantages**:
- Can get trapped in infinite loops
- No optimality guarantee
- Poor performance on deep search spaces

### 2. Breadth First Search (BFS)

**Algorithm**: Explores all nodes at the current depth level before moving to the next depth level.

```python
from state_space_search.breadth_first_search import bfs

# Find shortest path
result = bfs(start='A', target='J')
print(result)  # Output: Optimal path A -> ... -> J
```

**Characteristics**:
- **Time Complexity**: O(b^d) where d is depth of solution
- **Space Complexity**: O(b^d) - exponential space
- **Complete**: Yes (if branching factor is finite)
- **Optimal**: Yes (for uniform step costs)

**Advantages**:
- Guarantees optimal solution
- Complete algorithm
- Systematic exploration

**Disadvantages**:
- High memory requirements
- Slow for large search spaces
- Explores many irrelevant nodes

Here’s a minimal addition to your documentation to include **Depth-Bounded DFS** (also called *Limited Depth DFS*), **without changing anything unnecessarily** in your original content.

---

### 3. Depth-Bounded Depth First Search (D-DFS)

**Algorithm**: DFS with a fixed maximum depth limit. Avoids infinite loops in deep or cyclic graphs.

```python
from state_space_search.depth_bounded_dfs import depth_bounded_dfs

# DFS with depth limit
result = depth_bounded_dfs(start='A', target='J', max_depth=5)
print(result)  # Output: Path if within depth, otherwise None
```

**Characteristics**:

* **Time Complexity**: O(b^l) where *l* is depth limit
* **Space Complexity**: O(bl) - linear in depth limit
* **Complete**: No (if solution is beyond depth limit)
* **Optimal**: No

**Advantages**:

* Prevents infinite descent in cyclic/deep graphs
* Lower memory use
* Useful as a building block (e.g., for DFID)

**Disadvantages**:

* May miss solutions deeper than limit
* Requires choosing a good depth limit

---

### 🔧 Configuration

#### Additional Parameter

* `max_depth`: Integer specifying maximum depth to explore (for `depth_bounded_dfs`)

---

### 🏗️ Implementation Details

Ensure your new module `depth_bounded_dfs.py` follows the same interface:

```python
@test
def depth_bounded_dfs(start='A', target='J', alt=False, max_depth=5):
    # Bounded DFS implementation
    ...
```

---

### Example Usage

```python
# Bounded DFS with depth limit
path = depth_bounded_dfs(start='A', target='V', max_depth=4)
print(f"D-DFS Path (depth=4): {path}")
```

---


---

Let me know if you want the `depth_bounded_dfs.py` implementation too.




### 4. Depth First Iterative Deepening (DFID)

**Algorithm**: Combines benefits of DFS and BFS by performing DFS with increasing depth limits.

```python
from state_space_search.iterative_deepening import dfid

# Optimal search with linear space
result = dfid(start='A', target='J', max_depth=10)
print(result)  # Output: Optimal path with space efficiency
```

**Characteristics**:
- **Time Complexity**: O(b^d) - same as BFS
- **Space Complexity**: O(bd) - linear like DFS
- **Complete**: Yes
- **Optimal**: Yes (for uniform costs)

**Advantages**:
- Optimal like BFS
- Space-efficient like DFS
- No need to know depth limit in advance

**Disadvantages**:
- Redundant computation at each iteration
- Slightly more time than BFS due to repeated work

## 🏗️ Implementation Details

### Graph Structure

The algorithms use a graph representation supporting:

```python
class Graph:
    def __init__(self, target='H', alt=False):
        # Two graph configurations available
        # Default: 26-node alphabet graph
        # Alt: 5-node simple graph
    
    def neighbors(self, node):
        # Returns adjacent nodes
    
    def goal(self, node):
        # Tests if node is the target
    
    def reconstruct(self, nodes):
        # Builds path from parent-child pairs
```

### Common Pattern

All algorithms follow this pattern:

1. **Initialize**: Set up data structures (stack/queue, visited set)
2. **Loop**: While frontier is not empty:
   - Extract next node to explore
   - Check if goal reached
   - Add neighbors to frontier
   - Track visited nodes
3. **Reconstruct**: Build solution path

### Testing Framework

Each algorithm uses the `@test` decorator for performance measurement:

```python
@test
def dfs(start='A', target='J', alt=False):
    # Algorithm implementation
    # Returns path string or None if no solution
```

## 📊 Performance Comparison

| Algorithm | Time   | Space  | Complete | Optimal | Use Case                               |
|-----------| ------ | ------ | -------- | ------- | -------------------------------------- |
| DFS       | O(b^m) | O(bm)  | No       | No      | Deep solutions, memory limited         |
| BFS       | O(b^d) | O(b^d) | Yes      | Yes\*   | Shallow solutions, optimality needed   |
| DFID      | O(b^d) | O(bd)  | Yes      | Yes\*   | Best of both worlds                    |
| DB-DFS    | O(b^l) | O(bl)  | No       | No      | Controlled search depth, fast fallback |

*Optimal for uniform step costs

## 🎯 Usage Examples

### Example 1: Basic Path Finding
```python
# Find any path from A to V
path = dfs(start='A', target='V')
print(f"DFS Path: {path}")

# Find shortest path
path = bfs(start='A', target='V')
print(f"BFS Path: {path}")
```

### Example 2: Comparing Performance
```python
import time

# DFS - Fast but not optimal
start_time = time.time()
dfs_path = dfs('A', 'Z')
dfs_time = time.time() - start_time

# BFS - Slower but optimal
start_time = time.time()
bfs_path = bfs('A', 'Z')
bfs_time = time.time() - start_time

print(f"DFS: {dfs_path} (Time: {dfs_time:.4f}s)")
print(f"BFS: {bfs_path} (Time: {bfs_time:.4f}s)")
```

### Example 3: Handling Different Graph Structures
```python
# Default 26-node graph
result1 = dfs(start='A', target='Z', alt=False)

# Simple 5-node graph
result2 = dfs(start='A', target='E', alt=True)
```

## 🔧 Configuration

### Graph Selection
- `alt=False`: 26-node alphabet graph (default)
- `alt=True`: 5-node simple graph for testing

### Parameters
- `start`: Starting node (string)
- `target`: Goal node (string)
- `max_depth`: Maximum depth for DFID (integer)

## 🚀 Extensions

Consider implementing:
- **Bidirectional Search**: Search from both start and goal
- **Uniform Cost Search**: Weighted edges support
- **Limited Discrepancy Search**: Bounded deviation from heuristic
- **Beam Search**: Limited width BFS

## 📚 Further Reading

- "Artificial Intelligence: A Modern Approach" by Russell & Norvig
- "Algorithms" by Cormen, Leiserson, Rivest & Stein
- Korf, R.E. "Depth-first iterative-deepening: An optimal admissible tree search"

## 🤝 Contributing

To add new state space search algorithms:
1. Follow the established pattern
2. Include comprehensive testing
3. Document time/space complexity
4. Provide usage examples