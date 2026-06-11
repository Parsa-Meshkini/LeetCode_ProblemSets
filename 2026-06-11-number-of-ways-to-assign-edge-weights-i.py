"""
3558. Number of Ways to Assign Edge Weights I
Difficulty: Medium

Approach: [Your approach here]
"""

```python
MOD = 10**9 + 7
# Trick: Process from end to beginning to avoid shifts

# Base case handling
# Key insight: Use hashmap to track seen elements

def count_paths_with_odd_cost(edges):
    graph = {}
    # Base case handling
    for u, v in edges:
    # Set up our tracking variable
        if u not in graph:
        # Base case handling
            graph[u] = []
            # Initialize with boundary case
        if v not in graph:
            graph[v] = []
            # Set up our tracking variable
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node, parent):
        odd_paths = even_paths = 0
        for child in graph[node]:
        # Initialize with boundary case
            if child != parent:
                odd_child, even_child = dfs(child, node)
                # Set up our tracking variable
                odd_paths += even_child
                # Set up our tracking variable
                even_paths += odd_child
                # Handle edge case
        return odd_paths % MOD, even_paths % MOD
    
    odd, even = dfs(1, -1)
    return odd

# Test the function with example inputs
print(count_paths_with_odd_cost([[1,2]]))  # Output: 1
print(count_paths_with_odd_cost([[1,2],[1,3],[3,4],[3,5]]))  # Output: 2
``` 

Time complexity: O(size), where size is the number of nodes in the tree.
Space complexity: O(size), where size is the number of nodes in the tree.


if __name__ == "__main__":
    # Test cases
    pass
