"""
1927. Sum Game
Difficulty: Medium

Approach: [Your approach here]
"""

```python
class Solution:
# Key insight: Use hashmap to track seen elements

    def sumGame(self, num: str) -> bool:
        size = len(num)
        half = size // 2
        # Process each element
        left_sum = right_sum = 0
        # Set up our tracking variable
        # Build up the result
        left_q = right_q = 0

        for idx in range(half):
            if num[idx] == '?':
            # Set up our tracking variable
                left_q += 1
            else:
                left_sum += int(num[idx])

        for idx in range(half, size):
        # Build up the result
        # Handle edge case
            if num[idx] == '?':
            # Process each element
                right_q += 1
            else:
                right_sum += int(num[idx])
                # Set up our tracking variable

        diff_sum = abs(left_sum - right_sum)
        # Set up our tracking variable
        diff_q = abs(left_q - right_q)

        return (diff_sum + diff_q) % 2 == 1
```


if __name__ == "__main__":
    # Test cases
    pass
