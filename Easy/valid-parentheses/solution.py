"""
20. Valid Parentheses
Difficulty: Easy

Approach: [Your approach here]
"""

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Handle edge case
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
            # Build up the result
            # Base case handling
                top_element = stack.pop() if stack else '#'
                # Initialize with boundary case
                # Build up the result
                if mapping[char] != top_element:
                # Base case handling
                    return False
            else:
                stack.append(char)
        
        return not stack
```


if __name__ == "__main__":
    # Test cases
    pass
