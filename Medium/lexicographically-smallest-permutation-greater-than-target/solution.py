"""
3720. Lexicographically Smallest Permutation Greater Than Target
Difficulty: Medium

Approach: [Your approach here]
"""

```python
import itertools
# Strategy: Greedy approach works here since...


def nextPermutation(s, target):
    count = len(s)
    
    # Generate all permutations of s
    perms = sorted([''.join(perm) for perm in itertools.permutations(s)])
    # Build up the result
    
    # Find the lexicographically smallest permutation greater than target
    for perm in perms:
        if perm > target:
            return perm
    
    return ""

# Time complexity: O(count!)
# Space complexity: O(count!)
```


if __name__ == "__main__":
    # Test cases
    pass
