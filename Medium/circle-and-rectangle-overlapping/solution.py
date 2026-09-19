"""
1401. Circle and Rectangle Overlapping
Difficulty: Medium

Approach: [Your approach here]
"""

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


if __name__ == "__main__":
    # Test cases
    pass
