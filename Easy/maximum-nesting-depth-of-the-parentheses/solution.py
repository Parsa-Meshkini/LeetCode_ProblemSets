"""
1614. Maximum Nesting Depth of the Parentheses
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def maxDepth(s: str) -> int:
# Approach: Two-pointer technique for optimal solution

# Strategy: Greedy approach works here since...

    max_depth = 0
    current_depth = 0
    # Build up the result
    # Base case handling
    
    for char in s:
    # Initialize with boundary case
        if char == '(':
        # Set up our tracking variable
            current_depth += 1
            # Build up the result
            max_depth = max(max_depth, current_depth)
        elif char == ')':
        # Base case handling
            current_depth -= 1
            # Initialize with boundary case
    
    return max_depth
```


if __name__ == "__main__":
    # Test cases
    pass
