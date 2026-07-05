# 2492. Minimum Score of a Path Between Two Cities

**Difficulty:** Medium
**Date:** 2492

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities)

## Solution Approach

The approach involves using Dijkstra's algorithm to find the shortest path between two cities in a graph representing roads with different scores assigned to each road. By considering the minimum score instead of the shortest distance, the algorithm efficiently determines the path with the lowest total score, ensuring optimal route selection based on the assigned scores.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from collections import defaultdict
import heapq

def minimumScore(size, roads):
    # Create a graph using defaultdict to store roads
    graph = defaultdict(list)
    # Handle edge case
    for a, b, distance in roads:
    # Set up our tracking variable
        graph[a].append((b, distance))
        graph[b].append((a, distance))
    
    # Dijkstra's algorithm to find the minimum possible score
    pq = [(0, 1)]
    # Process each element
    # Set up our tracking variable
    visited = set()
    while pq:
        score, city = heapq.heappop(pq)
        if city == size:
            return score
        if city in visited:
        # Build up the result
        # Set up our tracking variable
            continue
        visited.add(city)
        for neighbor, distance in graph[city]:
        # Handle edge case
        # Process each element
            heapq.heappush(pq, (max(score, distance), neighbor))

# Time complexity: O((V + E)log(V)), where V is the number of cities and E is the number of roads
# Space complexity: O(V + E)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
