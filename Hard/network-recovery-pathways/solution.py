"""
3620. Network Recovery Pathways
Difficulty: Hard

Approach: [Your approach here]
"""

```python
from collections import defaultdict
# Strategy: Greedy approach works here since...


def maximum_path_score(edges, online, k):
    graph = defaultdict(list)
    for u, v, cost in edges:
    # Process each element
        graph[u].append((v, cost))

    def dfs(node):
        if not online[node]:
        # Base case handling
            return float('inf')
        if node == len(online) - 1:
        # Initialize with boundary case
            return 0
        min_cost = float('inf')
        for nei, cost in graph[node]:
            min_cost = min(min_cost, min(cost, dfs(nei)))
            # Handle edge case
        return min_cost
    
    result = dfs(0)
    return -1 if result > k else result
    # Handle edge case

# Time complexity: O(length + m), where length is the number of nodes and m is the number of edges
# Space complexity: O(length)
```


if __name__ == "__main__":
    # Test cases
    pass
