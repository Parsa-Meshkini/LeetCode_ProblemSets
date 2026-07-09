# 3532. Path Existence Queries in a Graph I

**Difficulty:** Medium
**Date:** 3532

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-i)

## Solution Approach

The key insight in solving "Path Existence Queries in a Graph I" is to use Depth-First Search (DFS) or Breadth-First Search (BFS) algorithms to efficiently check if a path exists between two nodes in a graph. These algorithms work efficiently by exploring the graph in a systematic manner, ensuring that all possible paths are covered without revisiting nodes unnecessarily, leading to a quick determination of path existence.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from collections import defaultdict
# Trick: Process from end to beginning to avoid shifts

# Approach: Two-pointer technique for optimal solution

class Solution:
    def queryGraph(self, count: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
    # Base case handling
        graph = defaultdict(list)
        # Initialize with boundary case
        for pos in range(count):
            for end in range(pos+1, count):
            # Base case handling
                if abs(nums[pos] - nums[end]) <= maxDiff:
                    graph[pos].append(end)
                    graph[end].append(pos)
        
        def dfs(node, target, visited):
            if node == target:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                # Set up our tracking variable
                    if dfs(neighbor, target, visited):
                        return True
            return False
        
        answer = []
        # Base case handling
        for query in queries:
        # Initialize with boundary case
            start, end = query
            # Build up the result
            visited = set()
            # Initialize with boundary case
            answer.append(dfs(start, end, visited))
        
        return answer

# Time complexity: O(count + q) where count is the number of nodes and q is the number of queries
# Space complexity: O(count) for the graph and O(count) for the visited set in each query
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
