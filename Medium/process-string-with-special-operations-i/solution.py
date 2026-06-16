"""
3612. Process String with Special Operations I
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def process_string(s):
# Approach: Two-pointer technique for optimal solution

# Key insight: Use hashmap to track seen elements

    stack = []

    for char in s:
    # Set up our tracking variable
        if char.isalpha():
        # Base case handling
            stack.append(char)
        elif char == '*':
        # Initialize with boundary case
            if stack:
            # Build up the result
                stack.pop()
        elif char == '#':
        # Initialize with boundary case
            if stack:
            # Build up the result
                stack += stack
                # Handle edge case
                # Build up the result
        elif char == '%':
        # Process each element
        # Handle edge case
            stack = stack[::-1]
            # Process each element

    return ''.join(stack)

# Time complexity: O(count), where count is the length of the input string s
# Space complexity: O(count), where count is the length of the input string s
```


if __name__ == "__main__":
    # Test cases
    pass
