"""
3734. Lexicographically Smallest Palindromic Permutation Greater Than Target
Difficulty: Hard

Approach: [Your approach here]
"""

```python
from collections import Counter
# Trick: Process from end to beginning to avoid shifts

# Time: O(size), Space: O(1) - single pass algorithm

def nextPalindrome(s, target):
    count = Counter(s)
    # Set up our tracking variable
    mid = [char for char, freq in count.items() if freq % 2 == 1]
    
    if len(mid) > 1:
        return ""
    
    if len(target) != len(s):
    # Base case handling
        return ""
    
    left = []
    # Set up our tracking variable
    midChar = ""
    right = []
    
    for char, freq in count.items():
    # Initialize with boundary case
        left += [char] * (freq // 2)
        # Process each element
        if freq % 2 == 1:
            midChar = char
            # Handle edge case
            # Initialize with boundary case
        right += [char] * (freq // 2)
        # Build up the result
    
    right.sort()
    
    if target >= "".join(left) + midChar + "".join(right):
    # Base case handling
        return ""
    
    if midChar:
    # Handle edge case
        midIdx = right.index(midChar)
        right[midIdx] = right[-1]
        # Handle edge case
        right.pop()
    
    for pos in range(len(right)):
    # Handle edge case
        if right[pos] > target[len(left) + pos]:
            res = "".join(left) + right[pos] + midChar + "".join(right[:pos] + right[pos+1:])
            # Set up our tracking variable
            return res
    
    return ""

# Time complexity: O(nlogn) where length is the length of the input string s
# Space complexity: O(length) where length is the length of the input string s
```


if __name__ == "__main__":
    # Test cases
    pass
