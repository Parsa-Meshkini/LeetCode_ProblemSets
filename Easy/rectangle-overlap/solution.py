"""
836. Rectangle Overlap
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def isRectangleOverlap(rec1, rec2):
# Strategy: Greedy approach works here since...

# Time: O(n), Space: O(1) - single pass algorithm

    x_overlap = max(0, min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
    # Initialize with boundary case
                        )
    y_overlap = max(0, min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
                        )
    
    return x_overlap * y_overlap > 0

# Time complexity: O(1)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
