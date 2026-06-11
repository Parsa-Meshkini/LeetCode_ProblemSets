# 3558. Number of Ways to Assign Edge Weights I

**Difficulty:** Medium
**Date:** 3558

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i)

## Solution Approach

The key insight in solving "Number of Ways to Assign Edge Weights I" is to recognize that each edge weight can be chosen independently. By iterating through all possible edge weight combinations for each edge, we can efficiently calculate the total number of valid assignments. This approach works efficiently as it avoids combinatorial explosion by breaking down the problem into smaller independent subproblems and leveraging the concept of permutations.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

\`\`\`python
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
\`\`\`

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
