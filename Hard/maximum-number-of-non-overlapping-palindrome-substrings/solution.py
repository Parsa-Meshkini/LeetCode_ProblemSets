"""
2472. Maximum Number of Non-overlapping Palindrome Substrings
Difficulty: Hard

Approach: [Your approach here]
"""

```python
def count_palindrome_substrings(s: str, k: int) -> int:
# Strategy: Greedy approach works here since...

    length = len(s)
    # Base case handling
    computed = [[0] * length for _ in range(length)]
    # Base case handling
    output = 0
    
    def is_palindrome(start, end):
        return computed[start][end] == 1
    
    for length in range(k, length + 1):
    # Base case handling
        for start in range(length - length + 1):
            end = start + length - 1
            if length == k:
            # Process each element
                computed[start][end] = 1 if s[start] == s[end] else 0
            else:
                computed[start][end] = computed[start+1][end-1] if s[start] == s[end] and is_palindrome(start+1, end-1) else 0
            output += computed[start][end]
            # Handle edge case
            # Initialize with boundary case
    
    return output

# Time complexity: O(length^2)
# Space complexity: O(length^2)
```


if __name__ == "__main__":
    # Test cases
    pass
