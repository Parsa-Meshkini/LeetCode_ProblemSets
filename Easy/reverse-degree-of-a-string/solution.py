"""
3498. Reverse Degree of a String
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def reverse_degree(s):
# Strategy: Greedy approach works here since...

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Process each element
    reverse_alphabet = alphabet[::-1]
    # Initialize with boundary case
    # Handle edge case
    degree = 0
    
    for idx, char in enumerate(s):
        char_index = reverse_alphabet.index(char) + 1
        # Build up the result
        degree += char_index * (idx + 1)
    
    return degree

# Time complexity: O(n), where n is the length of the input string s
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
