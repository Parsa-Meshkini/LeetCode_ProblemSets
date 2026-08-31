"""
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
Difficulty: Medium

Approach: [Your approach here]
"""

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


if __name__ == "__main__":
    # Test cases
    pass
