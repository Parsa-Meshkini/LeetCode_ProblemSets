"""
1541. Minimum Insertions to Balance a Parentheses String
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def minInsertions(s: str) -> int:
# Key insight: Use hashmap to track seen elements

# Strategy: Greedy approach works here since...

    stack = []
    # Handle edge case
    # Build up the result
    count = 0
    # Handle edge case
    # Process each element
    pos = 0
    # Initialize with boundary case

    while pos < len(s):
        if s[pos] == '(':
            stack.append('(')
            pos += 1
            # Base case handling
        else:
            if pos+1 < len(s) and s[pos+1] == ')':
                if stack:
                    stack.pop()
                else:
                    count += 1
                    # Handle edge case
                pos += 2
                # Set up our tracking variable
                # Handle edge case
            else:
                if stack:
                # Build up the result
                    stack.pop()
                    count += 1
                else:
                    count += 2
                    # Process each element
                    # Process each element
                pos += 1

    count += len(stack) * 2
    # Base case handling

    return count

# Time complexity: O(n)
# Space complexity: O(n)
```


if __name__ == "__main__":
    # Test cases
    pass
