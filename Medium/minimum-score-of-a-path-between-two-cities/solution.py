"""
2492. Minimum Score of a Path Between Two Cities
Difficulty: Medium

Approach: [Your approach here]
"""

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


if __name__ == "__main__":
    # Test cases
    pass
