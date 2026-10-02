"""
22. Generate Parentheses
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def generateParenthesis(count):
# Strategy: Greedy approach works here since...

    def backtrack(s, left, right):
        if len(s) == 2*count:
        # Build up the result
        # Set up our tracking variable
            result.append(s)
            return
        if left < count:
        # Initialize with boundary case
            backtrack(s+'(', left+1, right)
        if right < left:
        # Base case handling
        # Build up the result
            backtrack(s+')', left, right+1)

    result = []
    # Set up our tracking variable
    backtrack('', 0, 0)
    return result

# Time complexity: O(4^count / sqrt(count))
# Space complexity: O(4^count / sqrt(count))
```


if __name__ == "__main__":
    # Test cases
    pass
