# Artificial Intelligence :  Search Algorithms Implementation

A comprehensive collection of artificial intelligence search algorithms implemented in Python, covering state space search, heuristic methods, optimization techniques, and game theory.

## 📁 Repository Structure

```
ai-search-algorithms/
├── README.md
├── requirements.txt
├── utils/
│   ├── __init__.py
│   ├── graph.py
│   └── test.py
├── state_space_search/
│   ├── README.md
│   ├── depth_first_search.py
│   ├── breadth_first_search.py
│   └── iterative_deepening.py
├── heuristic_search/
│   ├── README.md
│   ├── best_first_search.py
│   ├── hill_climbing.py
│   ├── stochastic_local_search.py
│   └── traveling_salesman/
├── population_methods/
│   ├── README.md
│   ├── genetic_algorithms.py
│   ├── ant_colony_optimization.py
│   └── satisfiability/
├── optimal_path_finding/
│   ├── README.md
│   ├── branch_and_bound.py
│   ├── a_star.py
│   ├── weighted_a_star.py
│   ├── ida_star.py
│   └── recursive_best_first.py
├── game_playing/
│   ├── README.md
│   ├── minimax.py
│   ├── alpha_beta.py
│   └── sss_star.py
├── automated_planning/
│   ├── README.md
│   ├── forward_backward_search.py
│   ├── goal_stack_planning.py
│   └── plan_space_planning.py
├── problem_decomposition/
│   ├── README.md
│   ├── means_ends_analysis.py
│   ├── graphplan.py
│   └── ao_star.py
├── expert_systems/
│   ├── README.md
│   ├── production_systems.py
│   ├── inference_engine.py
│   └── rete_net.py
├── logic_search/
│   ├── README.md
│   ├── forward_chaining.py
│   ├── backward_chaining.py
│   └── first_order_logic.py
└── constraint_processing/
    ├── README.md
    ├── backtracking.py
    ├── arc_consistency.py
    └── forward_checking.py
```

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-search-algorithms.git
   cd ai-search-algorithms
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run a basic example**
   ```python
   from state_space_search.depth_first_search import dfs
   
   # Find path from A to J
   result = dfs(start='A', target='J')
   print(result)
   ```

## 🔍 Algorithm Categories

### 1. **State Space Search**
- **Depth First Search (DFS)**: Explores as far as possible along each branch before backtracking
- **Breadth First Search (BFS)**: Explores all nodes at present depth before moving to next depth level
- **Iterative Deepening**: Combines benefits of DFS and BFS with space efficiency

### 2. **Heuristic Search**
- **Best First Search**: Uses heuristic function to guide search towards goal
- **Hill Climbing**: Local search that moves towards better neighboring states
- **Stochastic Local Search**: Introduces randomness to escape local optima
- **Traveling Salesman Problem**: Classic optimization problem implementations

### 3. **Population-Based Methods**
- **Genetic Algorithms**: Evolution-inspired optimization using selection, crossover, and mutation
- **Ant Colony Optimization**: Swarm intelligence for pathfinding and optimization
- **SAT Solvers**: Boolean satisfiability problem solving techniques

### 4. **Optimal Path Finding**
- **A\* Algorithm**: Best-first search using admissible heuristics for optimal solutions
- **Branch & Bound**: Systematic enumeration with pruning for optimization
- **Weighted A\***: Trading optimality for faster solutions
- **IDA\***: Memory-efficient iterative deepening A*
- **RBFS**: Recursive best-first search with linear space complexity

### 5. **Game Playing**
- **Minimax**: Optimal decision making for two-player zero-sum games
- **Alpha-Beta Pruning**: Optimization of minimax with branch pruning
- **SSS\***: State-space search for game trees

### 6. **Automated Planning**
- **STRIPS Planning**: Classical planning with preconditions and effects
- **Goal Stack Planning**: Subgoal-based planning approach
- **Plan Space Planning**: Partial order planning methods

### 7. **Problem Decomposition**
- **Means-Ends Analysis**: Problem solving by reducing differences
- **Graphplan**: Graph-based planning algorithm
- **AO\***: AND-OR graph search for decomposable problems

### 8. **Expert Systems**
- **Production Systems**: Rule-based inference mechanisms
- **Rete Algorithm**: Efficient pattern matching for rule engines
- **Inference Engines**: Forward and backward chaining implementations

### 9. **Logic-Based Search**
- **First-Order Logic**: Predicate logic reasoning systems
- **Resolution**: Automated theorem proving technique
- **Chaining Methods**: Forward and backward chaining for logical inference

### 10. **Constraint Processing**
- **Constraint Satisfaction Problems**: Systematic approaches to CSPs
- **Arc Consistency**: Local consistency algorithms
- **Backtracking**: Systematic search with constraint propagation

## 🧪 Testing

Each algorithm includes comprehensive tests and benchmarking:

```python
from utils.test import test

@test
def your_algorithm():
    # Implementation here
    pass
```

## 📊 Performance Analysis

The repository includes performance analysis tools for:
- Time complexity measurements
- Space complexity analysis
- Solution quality evaluation
- Comparative benchmarking

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/algorithm-name`)
3. Implement your algorithm following the established patterns
4. Add comprehensive tests and documentation
5. Submit a pull request

## 📝 Documentation

Each algorithm family has detailed documentation including:
- Theoretical background
- Implementation details
- Time and space complexity
- Usage examples
- Performance characteristics

## 🔗 References

- Russell, S. & Norvig, P. "Artificial Intelligence: A Modern Approach"
- Korf, R. E. "Depth-first iterative-deepening: An optimal admissible tree search"
- Hart, P. E., Nilsson, N. J. & Raphael, B. "A Formal Basis for the Heuristic Determination of Minimum Cost Paths"

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏷️ Tags

`artificial-intelligence` `search-algorithms` `python` `graph-algorithms` `optimization` `heuristics` `game-theory` `constraint-satisfaction` `automated-planning` `expert-systems`