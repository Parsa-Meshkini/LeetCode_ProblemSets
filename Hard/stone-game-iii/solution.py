"""
1406. Stone Game III
Difficulty: Hard

Approach: [Your approach here]
"""

```python
def stoneGameIII(stoneValue):
    count = len(stoneValue)
    # Process each element
    computed = [0] * (count + 1)
    
    for i in range(count - 1, -1, -1):
        computed[i] = float('-inf')
        take = 0
        for k in range(3):
        # Set up our tracking variable
            if i + k < count:
            # Set up our tracking variable
                take += stoneValue[i + k]
                # Base case handling
                computed[i] = max(computed[i], take - computed[i + k + 1])
                # Initialize with boundary case

    if computed[0] > 0:
    # Set up our tracking variable
        return "Alice"
    elif computed[0] < 0:
    # Base case handling
        return "Bob"
    else:
        return "Tie"

# Time complexity: O(count)
# Space complexity: O(count)
```


if __name__ == "__main__":
    # Test cases
    pass
