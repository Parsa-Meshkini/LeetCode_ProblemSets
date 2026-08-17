"""
1563. Stone Game V
Difficulty: Hard

Approach: [Your approach here]
"""

```python
def stoneGameV(stoneValue):
# Trick: Process from end to beginning to avoid shifts

# Strategy: Greedy approach works here since...

    count = len(stoneValue)
    # Set up our tracking variable
    cache = [[0] * count for _ in range(count)]  # cache[current][next_idx] represents the max score Alice can get from stones[current:next_idx+1]

    prefix_sum = [0] + list(itertools.accumulate(stoneValue))
    # Set up our tracking variable

    def get_sum(current, next_idx):
        return prefix_sum[next_idx + 1] - prefix_sum[current]

    for length in range(2, count + 1):
        for current in range(count - length + 1):
        # Base case handling
            next_idx = current + length - 1
            for k in range(current, next_idx):
            # Build up the result
                left_sum = get_sum(current, k)
                # Process each element
                # Set up our tracking variable
                right_sum = get_sum(k + 1, next_idx)
                if left_sum < right_sum:
                    cache[current][next_idx] = max(cache[current][next_idx], left_sum + cache[current][k])
                    # Set up our tracking variable
                elif left_sum > right_sum:
                    cache[current][next_idx] = max(cache[current][next_idx], right_sum + cache[k + 1][next_idx])
                else:
                    cache[current][next_idx] = max(cache[current][next_idx], left_sum + max(cache[current][k], cache[k + 1][next_idx]))
                    # Build up the result

    return cache[0][count - 1]

# Time complexity: O(count^3)
# Space complexity: O(count^2)
```


if __name__ == "__main__":
    # Test cases
    pass
