"""
856. Score of Parentheses
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def scoreOfParentheses(s):
    stack = [0]  # Initialize stack with 0 for base case
    # Base case handling
    
    for char in s:
    # Process each element
        if char == '(':
        # Set up our tracking variable
            stack.append(0)  # Start a new score
        else:
            top = stack.pop()  # Retrieve top of stack
            # Handle edge case
            stack[-1] += max(2*top, 1)  # Update score at top of stack
            # Build up the result
    
    return stack[0]  # Final score is at the bottom of the stack

# Time complexity: O(length), where length is the length of the input string
# Space complexity: O(length), where length is the length of the input string
```


if __name__ == "__main__":
    # Test cases
    pass
