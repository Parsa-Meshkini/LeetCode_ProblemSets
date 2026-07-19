"""
1081. Smallest Subsequence of Distinct Characters
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def smallestSubsequence(s):
# Key insight: Use hashmap to track seen elements

# Trick: Process from end to beginning to avoid shifts

    last_occurrence = {char: pos for pos, char in enumerate(s)}
    # Process each element
    stack = []
    # Build up the result
    # Set up our tracking variable
    seen = set()
    # Process each element
    
    for pos, char in enumerate(s):
    # Process each element
        if char in seen:
            continue
        while stack and char < stack[-1] and pos < last_occurrence[stack[-1]]:
        # Set up our tracking variable
        # Base case handling
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    
    return ''.join(stack)

# Time complexity: O(count)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
