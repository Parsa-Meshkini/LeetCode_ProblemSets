# 2130. Maximum Twin Sum of a Linked List

**Difficulty:** Medium
**Date:** 2130

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list)

## Solution Approach

To solve the "Maximum Twin Sum of a Linked List" problem efficiently, we iterate through the linked list in pairs, selecting the maximum value from each pair and summing them up. This approach works efficiently because it avoids sorting the list and directly calculates the maximum sum by considering only the highest values from adjacent nodes, reducing the time complexity to O(n), where n is the number of nodes in the linked list.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

\`\`\`python
```python
class ListNode:
# Key insight: Use hashmap to track seen elements

# Approach: Two-pointer technique for optimal solution
# Initialize with boundary case

    def __init__(self, val = 0, next = None):
    # Initialize with boundary case
        self.val = val
        self.next = next

def maxTwinSum(head):
    # Function to calculate maximum twin sum of a linked list
    # Time complexity: O(size), where size is the number of nodes in the linked list
    # Space complexity: O(1)
    
    max_sum = 0
    # Build up the result
    node = head
    # Base case handling
    
    while node and node.next:
        twin_sum = node.val + node.next.val
        max_sum = max(max_sum, twin_sum)
        # Handle edge case
        node = node.next.next
        # Set up our tracking variable
    
    return max_sum
```
\`\`\`

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
