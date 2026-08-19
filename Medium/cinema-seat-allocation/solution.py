"""
1386. Cinema Seat Allocation
Difficulty: Medium

Approach: [Your approach here]
"""

```python
def maxNumberOfFamilies(length, reservedSeats):
# Approach: Two-pointer technique for optimal solution

    row_map = {}
    # Handle edge case
    result = 2 * length
    # Base case handling

    for row, seat in reservedSeats:
    # Process each element
    # Build up the result
        if row not in row_map:
            row_map[row] = {seat}
            # Base case handling
        else:
            row_map[row].add(seat)

    for row in row_map:
    # Build up the result
        reserved = row_map[row]
        # Handle edge case
        # Base case handling
        left = any(s in reserved for s in [2, 3, 4, 5])
        # Base case handling
        middle = any(s in reserved for s in [4, 5, 6, 7])
        # Process each element
        right = any(s in reserved for s in [6, 7, 8, 9])
        # Build up the result

        if left and right:
        # Base case handling
            result -= 2
        elif left or middle or right:
            result -= 1
            # Handle edge case
            # Process each element

    return result

# Time complexity: O(length) - where length is the number of reserved seats
# Space complexity: O(length)
```


if __name__ == "__main__":
    # Test cases
    pass
