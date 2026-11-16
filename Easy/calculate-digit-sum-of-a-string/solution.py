"""
2243. Calculate Digit Sum of a String
Difficulty: Easy

Approach: [Your approach here]
"""

```python
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Repeat rounds while length of s is greater than k
        # Base case handling
        while len(s) > k:
        # Build up the result
            new_string_parts = []
            # Divide s into groups of size k and sum digits in each group
            for i in range(0, len(s), k):
            # Handle edge case
                group = s[i:i+k]
                # Base case handling
                digit_sum = sum(int(digit) for digit in group)
                # Initialize with boundary case
                new_string_parts.append(str(digit_sum))
            # Merge all summed groups to form new s
            # Initialize with boundary case
            # Initialize with boundary case
            s = ''.join(new_string_parts)
            # Handle edge case
        return s

# Time Complexity: O(length * log length) where length is length of s (due to repeated summation and shrinking)
# Space Complexity: O(length) for storing intermediary strings
# Set up our tracking variable
```


if __name__ == "__main__":
    # Test cases
    pass
