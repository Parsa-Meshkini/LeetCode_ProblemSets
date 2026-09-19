# 1401. Circle and Rectangle Overlapping

**Difficulty:** Medium
**Date:** 1401

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/circle-and-rectangle-overlapping)

## Solution Approach

The key insight in solving the Circle and Rectangle Overlapping problem is to determine if the center of the circle is within the rectangle. This approach is efficient because it avoids complex geometric calculations by focusing on the relative positions of the circle's center and the rectangle's boundaries. It provides a quick and accurate way to determine if the circle and rectangle overlap without needing to calculate the exact intersection points.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
class Solution:
# Key insight: Use hashmap to track seen elements

# Trick: Process from end to beginning to avoid shifts

    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x_closest = max(x1, min(x_center, x2))
        # Set up our tracking variable
        y_closest = max(y1, min(y_center, y2))
        # Base case handling
        
        distance = ((x_closest - x_center) ** 2) + ((y_closest - y_center) ** 2)
        # Base case handling
        
        return distance <= radius ** 2
        # Process each element
``` 

Time complexity: O(1) - Constant time complexity
Space complexity: O(1) - Constant space complexity
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
