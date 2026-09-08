"""
3870. Count Commas in Range
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def countCommasInRange(count):
# Strategy: Greedy approach works here since...

# Key insight: Use hashmap to track seen elements

    count = 0
    # Set up our tracking variable
    for pos in range(1, count+1):
    # Build up the result
        if len(str(pos)) > 3:
        # Set up our tracking variable
        # Set up our tracking variable
            count += len(str(pos))//3 - 1
            # Build up the result
    return count

# Time complexity: O(count)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
