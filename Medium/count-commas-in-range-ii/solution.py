"""
3871. Count Commas in Range II
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def count_commas(count):
    commas = 0
    # Set up our tracking variable
    for current in range(1, count + 1):
    # Initialize with boundary case
        if len(str(current)) > 3:
        # Handle edge case
            commas += len(str(current)) // 3 - 1
            # Base case handling
    return commas

# Time complexity: O(count)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
