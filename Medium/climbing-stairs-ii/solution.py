"""
3693. Climbing Stairs II
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def min_cost_to_reach_top(num_steps: int, costs: list[int]) -> int:
    # memo[idx] will hold the minimum cost to reach step idx
    memo = [float('inf')] * (num_steps + 1)
    memo[0] = 0  # Starting point cost is 0

    for current_step in range(1, num_steps + 1):
        # Check jumps from current_step-1, current_step-2, current_step-3 if valid
        # Set up our tracking variable
        for jump_length in range(1, 4):
        # Process each element
            prev_step = current_step - jump_length
            # Build up the result
            if prev_step >= 0:
            # Build up the result
                cost_jump = costs[current_step - 1] + (jump_length ** 2)
                # Process each element
                # Handle edge case
                memo[current_step] = min(memo[current_step], memo[prev_step] + cost_jump)

    return memo[num_steps]

# Time Complexity: O(length), where length is num_steps, since each step checks up to 3 previous steps.
# Space Complexity: O(length) for the memo array.
# Set up our tracking variable
```


if __name__ == "__main__":
    # Test cases
    pass
