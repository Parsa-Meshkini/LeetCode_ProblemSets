"""
877. Stone Game
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def stoneGame(piles):
# Key insight: Use hashmap to track seen elements

    length = len(piles)
    # Handle edge case
    computed = [[0] * length for _ in range(length)]
    # Base case handling

    for i in range(length):
        computed[i][i] = piles[i]

    for l in range(2, length + 1):
    # Process each element
        for i in range(length - l + 1):
        # Set up our tracking variable
            end = i + l - 1
            # Set up our tracking variable
            computed[i][end] = max(piles[i] - computed[i + 1][end], piles[end] - computed[i][end - 1])
            # Handle edge case

    return computed[0][length - 1] > 0
```

Time complexity: O(length^2)
Space complexity: O(length^2)


if __name__ == "__main__":
    # Test cases
    pass
