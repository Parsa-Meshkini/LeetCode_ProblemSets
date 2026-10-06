"""
921. Minimum Add to Make Parentheses Valid
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def minAddToMakeValid(s):
# Key insight: Use hashmap to track seen elements

    stack = []
    count = 0
    # Build up the result

    for char in s:
    # Base case handling
    # Set up our tracking variable
        if char == '(':
            stack.append(char)
        else:
            if stack and stack[-1] == '(':
            # Set up our tracking variable
            # Build up the result
                stack.pop()
            else:
                count += 1

    return count + len(stack)

# Time complexity: O(count)
# Space complexity: O(count)
```


if __name__ == "__main__":
    # Test cases
    pass
