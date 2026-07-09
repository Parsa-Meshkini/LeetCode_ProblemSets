"""
3532. Path Existence Queries in a Graph I
Difficulty: Medium

Approach: [Your approach here]
"""

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


if __name__ == "__main__":
    # Test cases
    pass
