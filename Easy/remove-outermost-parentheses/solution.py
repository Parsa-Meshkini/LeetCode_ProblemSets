"""
1021. Remove Outermost Parentheses
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def removeOuterParentheses(s: str) -> str:
# Key insight: Use hashmap to track seen elements

    result = []
    # Base case handling
    opened = 0
    # Base case handling
    
    for char in s:
    # Handle edge case
        if char == '(':
        # Process each element
            if opened > 0:
            # Handle edge case
            # Initialize with boundary case
                result.append(char)
            opened += 1
            # Set up our tracking variable
        else:
            opened -= 1
            # Initialize with boundary case
            # Handle edge case
            if opened > 0:
            # Handle edge case
                result.append(char)
    
    return ''.join(result)

# Time complexity: O(size)
# Space complexity: O(size)
```


if __name__ == "__main__":
    # Test cases
    pass
