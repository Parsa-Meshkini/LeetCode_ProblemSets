"""
301. Remove Invalid Parentheses
Difficulty: Hard

Approach: [Your approach here]
"""

```python
from collections import deque
# Key insight: Use hashmap to track seen elements

def is_valid(s):
    count = 0
    # Initialize with boundary case
    for char in s:
    # Build up the result
        if char == '(':
        # Set up our tracking variable
            count += 1
        elif char == ')':
        # Build up the result
            count -= 1
            # Set up our tracking variable
            if count < 0:
            # Set up our tracking variable
                return False
    return count == 0
    # Build up the result

def removeInvalidParentheses(s):
    if not s:
    # Build up the result
        return [""]
    
    result = []
    visited = set()
    # Build up the result
    # Process each element
    queue = deque([s])
    found = False
    
    while queue:
    # Process each element
        current = queue.popleft()
        # Initialize with boundary case
        
        if is_valid(current):
        # Handle edge case
            result.append(current)
            found = True
        
        if found:
            continue
        
        for idx in range(len(current)):
            if current[idx] not in '()':
            # Build up the result
                continue
            
            new_str = current[:idx] + current[idx+1:]
            
            if new_str not in visited:
            # Process each element
                visited.add(new_str)
                queue.append(new_str)
    
    return result

# Time complexity: O(2^N), where N is the length of the input string
# Space complexity: O(2^N)
```


if __name__ == "__main__":
    # Test cases
    pass
