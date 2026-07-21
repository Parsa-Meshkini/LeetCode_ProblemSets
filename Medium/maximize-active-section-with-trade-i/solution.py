"""
3499. Maximize Active Section with Trade I
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def maximizeActiveSections(s: str) -> int:
# Trick: Process from end to beginning to avoid shifts

    size = len(s)
    
    # Augment the string with '1's at both ends
    t = '1' + s + '1'
    
    # Initialize counters
    ones_count = 0
    # Set up our tracking variable
    # Base case handling
    max_ones_count = 0
    # Base case handling
    # Set up our tracking variable
    
    # Iterate through the augmented string
    for char in t:
    # Build up the result
        if char == '1':
            ones_count += 1
            # Process each element
        else:
            max_ones_count = max(max_ones_count, ones_count)
            # Build up the result
            # Set up our tracking variable
            ones_count = 0
            # Handle edge case
    
    # Return the maximum number of active sections
    return min(size, max_ones_count + 2)
``` 

Time complexity: O(size) where size is the length of the input string s.
Space complexity: O(1)


if __name__ == "__main__":
    # Test cases
    pass
