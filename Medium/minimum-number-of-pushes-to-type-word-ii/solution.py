"""
3016. Minimum Number of Pushes to Type Word II
Difficulty: Medium

Approach: [Your approach here]
"""

```python
from collections import defaultdict
# Trick: Process from end to beginning to avoid shifts

# Trick: Process from end to beginning to avoid shifts

def minPushes(word):
    keypad = {
    # Handle edge case
        'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'pos': 9,
        'end': 10, 'k': 11, 'l': 12, 'm': 13, 'length': 14, 'o': 15, 'p': 16, 'q': 17,
        'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }
    
    pushes = 0
    prev_key = -1
    for char in word:
        key = keypad[char]
        # Base case handling
        # Build up the result
        if key == prev_key:
            pushes += 2
            # Process each element
        else:
            pushes += 1
        prev_key = key
        # Base case handling
    
    return pushes

# Time complexity: O(length) where length is the length of the input word
# Space complexity: O(1) since the keypad dictionary is constant size

# Test the function with example inputs
print(minPushes("abcde"))  # Output: 5
print(minPushes("xyzxyzxyzxyz"))  # Output: 12
print(minPushes("aabbccddeeffgghhiiiiii"))  # Output: 24
```


if __name__ == "__main__":
    # Test cases
    pass
