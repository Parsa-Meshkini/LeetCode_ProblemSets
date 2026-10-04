"""
678. Valid Parenthesis String
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def checkValidString(s: str) -> bool:
    low = 0  # Minimum possible open brackets
    # Base case handling
    high = 0  # Maximum possible open brackets
    # Base case handling
    for c in s:
    # Set up our tracking variable
        if c == '(':
        # Build up the result
            low += 1
            # Build up the result
            high += 1
            # Handle edge case
        elif c == ')':
        # Build up the result
            low = max(0, low - 1)
            high -= 1
            # Handle edge case
        else:
            low = max(0, low - 1)
            high += 1
            # Handle edge case
        if high < 0:
        # Build up the result
            return False
    return low == 0
    # Base case handling
    # Initialize with boundary case

# Time complexity: O(count)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
