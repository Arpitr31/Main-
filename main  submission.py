
### 2. `main.py`

```python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    # Your implementation goes here
    pass

# Helper function to perform topological sort
def topological_sort(graph):
    # Your implementation goes here
    pass

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    # Your implementation goes here
    pass
def find_longest_path(graph, topo_order):
    distances = [-float('inf')] * len(graph)
    # Initialize distances to all vertices as minus infinity
    # Here we assume we can start from any vertex
    for i in range(len(graph)):
        if distances[i] == -float('inf'):
            distances[i] = 0
    
    for u in topo_order:
        if distances[u] != -float('inf'):
            for v, weight in graph[u]:
                if distances[v] < distances[u] + weight:
                    distances[v] = distances[u] + weight
    
    return max(distances)


def topological_sort(graph):
    in_degree = [0] * len(graph)
    for u in range(len(graph)):
        for v, _ in graph[u]:
            in_degree[v] += 1
    
    zero_in_degree_queue = deque([i for i in range(len(graph)) if in_degree[i] == 0])
    topo_order = []
    
    while zero_in_degree_queue:
        u = zero_in_degree_queue.popleft()
        topo_order.append(u)
        for v, _ in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                zero_in_degree_queue.append(v)
    
    return topo_order

def longest_path(graph: list) -> int:
    from collections import deque
    
    def topological_sort(graph):
        in_degree = [0] * len(graph)
        for u in range(len(graph)):
            for v, _ in graph[u]:
                in_degree[v] += 1
        
        zero_in_degree_queue = deque([i for i in range(len(graph)) if in_degree[i] == 0])
        topo_order = []
        
        while zero_in_degree_queue:
            u = zero_in_degree_queue.popleft()
            topo_order.append(u)
            for v, _ in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    zero_in_degree_queue.append(v)
        
        return topo_order

    

    topo_order = topological_sort(graph)
    return find_longest_path(graph, topo_order)
