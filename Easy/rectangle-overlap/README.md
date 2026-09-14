# 836. Rectangle Overlap

**Difficulty:** Easy
**Date:** 836

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/rectangle-overlap)

## Solution Approach

To solve the "Rectangle Overlap" problem efficiently, we can determine if the rectangles do not overlap by checking if one rectangle is either completely to the left, right, above, or below the other. If they do not meet any of these conditions, then they must overlap. This approach works efficiently because it leverages simple comparisons along the x and y axes to quickly identify non-overlapping scenarios, avoiding the need for complex calculations.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
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
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
