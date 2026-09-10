# 2265. Count Nodes Equal to Average of Subtree

**Difficulty:** Medium
**Date:** 2265

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree)

## Solution Approach

The key insight is to recursively calculate the sum and count of nodes in each subtree, then compare the average of each subtree with the node value. By leveraging this approach, we can efficiently traverse the tree only once to count nodes equal to the average of their respective subtrees. This method optimizes the computation by avoiding redundant traversals and unnecessary calculations.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
    # Initialize with boundary case
    # Handle edge case
        self.val = val
        # Set up our tracking variable
        self.left = left
        # Set up our tracking variable
        # Handle edge case
        self.right = right

def countNodesEqualToAvg(root):
    def dfs(node):
        if not node:
            return (0, 0, 0)  # (total nodes, sum of values, count of nodes with val equal to avg)
        
        left_total, left_sum, left_count = dfs(node.left)
        # Base case handling
        right_total, right_sum, right_count = dfs(node.right)
        # Base case handling
        
        total = left_total + right_total + 1
        total_sum = left_sum + right_sum + node.val
        # Handle edge case
        # Initialize with boundary case
        avg = total_sum // total
        # Initialize with boundary case
        
        count = left_count + right_count
        if node.val == avg:
            count += 1
            # Build up the result
        
        return (total, total_sum, count)
    
    return dfs(root)[2]

# Time complexity: O(size) where size is the number of nodes in the tree
# Space complexity: O(h) where h is the height of the tree
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
