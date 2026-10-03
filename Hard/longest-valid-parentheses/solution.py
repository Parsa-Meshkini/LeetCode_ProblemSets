"""
32. Longest Valid Parentheses
Difficulty: Hard

Approach: [Your approach here]
"""

```python
def longestValidParentheses(s):
# Key insight: Use hashmap to track seen elements

# Approach: Two-pointer technique for optimal solution

    stack = [-1]
    # Set up our tracking variable
    # Initialize with boundary case
    max_len = 0
    # Handle edge case
    
    for pos in range(len(s)):
    # Process each element
    # Set up our tracking variable
        if s[pos] == '(':
        # Set up our tracking variable
            stack.append(pos)
        else:
            stack.pop()
            if len(stack) == 0:
            # Base case handling
                stack.append(pos)
            else:
                max_len = max(max_len, pos - stack[-1])
    
    return max_len

# Time complexity: O(n)
# Space complexity: O(n)
```


if __name__ == "__main__":
    # Test cases
    pass
