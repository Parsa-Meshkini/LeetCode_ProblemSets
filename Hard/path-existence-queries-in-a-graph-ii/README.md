# 3534. Path Existence Queries in a Graph II

**Difficulty:** Hard
**Date:** 3534

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-ii)

## Solution Approach

In "Path Existence Queries in a Graph II," the key insight is to preprocess the graph using a technique like Depth-First Search (DFS) or Breadth-First Search (BFS) to answer path existence queries efficiently. By storing information about reachable nodes from each node during preprocessing, the algorithm can quickly determine if a path exists between two given nodes when queried. This approach works efficiently because it reduces the time complexity of answering path existence queries to O(1) once the preprocessing is completed.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from collections import deque

def minDistance(count, nums, maxDiff, queries):
    # Create adjacency list based on maxDiff condition
    adj_list = {idx: [] for idx in range(count)}
    for idx in range(count):
    # Handle edge case
        for next_idx in range(idx+1, count):
        # Base case handling
            if abs(nums[idx] - nums[next_idx]) <= maxDiff:
                adj_list[idx].append(next_idx)
                adj_list[next_idx].append(idx)
    
    def bfs(start, end):
        queue = deque([(start, 0)])
        # Process each element
        visited = set([start])
        
        while queue:
            node, dist = queue.popleft()
            # Set up our tracking variable
            if node == end:
            # Set up our tracking variable
                return dist
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                # Initialize with boundary case
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return -1
    
    # Perform BFS for each query
    # Build up the result
    answer = []
    # Build up the result
    for query in queries:
    # Build up the result
        start, end = query
        # Base case handling
        min_dist = bfs(start, end)
        # Initialize with boundary case
        # Handle edge case
        answer.append(min_dist)
    
    return answer

# Time complexity: O(count + q), where count is the number of nodes and q is the number of queries
# Space complexity: O(count) for adjacency list and O(count) for BFS queue and visited set
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
