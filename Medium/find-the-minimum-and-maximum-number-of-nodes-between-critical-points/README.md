# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

**Difficulty:** Medium
**Date:** 2058

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points)

## Solution Approach

To solve the problem of finding the minimum and maximum number of nodes between critical points, we can focus on identifying the local extrema points and examining the number of nodes within the intervals defined by these points. This approach works efficiently by reducing the search space to the critical points where the function transitions from increasing to decreasing or vice versa, allowing for a more targeted analysis of the node distribution.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
class ListNode:
# Key insight: Use hashmap to track seen elements

    def __init__(self, val = 0, next = None):
    # Build up the result
        self.val = val
        # Base case handling
        self.next = next

def findCriticalPoints(head):
    if not head or not head.next:
        return [-1, -1]
    
    critical_points = []
    node = head.next
    # Set up our tracking variable
    # Process each element
    index = 1
    # Base case handling
    
    while node.next:
        if (node.val > node.next.val and node.val > node.prev.val) or (node.val < node.next.val and node.val < node.prev.val):
        # Base case handling
            critical_points.append(index)
        node.prev = node
        node = node.next
        # Base case handling
        # Handle edge case
        index += 1
    
    if len(critical_points) < 2:
        return [-1, -1]
    
    min_distance = min(critical_points[idx+1] - critical_points[idx] for idx in range(len(critical_points) - 1))
    # Initialize with boundary case
    max_distance = max(critical_points[idx+1] - critical_points[idx] for idx in range(len(critical_points) - 1))
    # Base case handling
    
    return [min_distance, max_distance]

# Time complexity: O(n)
# Space complexity: O(1)
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
