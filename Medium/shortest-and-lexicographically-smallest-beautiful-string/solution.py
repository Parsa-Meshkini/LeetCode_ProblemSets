"""
2904. Shortest and Lexicographically Smallest Beautiful String
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def shortestBeautifulString(s, k):
# Process each element
# Key insight: Use hashmap to track seen elements

    count = len(s)
    # Set up our tracking variable
    result = ""
    for current in range(count):
    # Set up our tracking variable
        cnt = 0
        for next_idx in range(current, count):
            if s[next_idx] == "1":
            # Base case handling
                cnt += 1
                # Build up the result
            if cnt == k:
            # Set up our tracking variable
                if not result or s[current:next_idx+1] < result:
                # Handle edge case
                    result = s[current:next_idx+1]
                    # Base case handling
                break
    return result

# Time complexity: O(count^2)
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
