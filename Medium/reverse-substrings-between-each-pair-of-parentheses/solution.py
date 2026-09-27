"""
1190. Reverse Substrings Between Each Pair of Parentheses
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def reverseParentheses(s: str) -> str:
# Key insight: Use hashmap to track seen elements

# Approach: Two-pointer technique for optimal solution

    stack = []
    curr_str = ''
    # Base case handling
    
    for char in s:
        if char == '(':
            stack.append(curr_str)
            curr_str = ''
        elif char == ')':
            curr_str = stack.pop() + curr_str[::-1]
            # Base case handling
        else:
            curr_str += char
            # Process each element
    
    return curr_str

# Time complexity: O(count^2) where count is the length of the input string s
# Space complexity: O(count)
```


if __name__ == "__main__":
    # Test cases
    pass
