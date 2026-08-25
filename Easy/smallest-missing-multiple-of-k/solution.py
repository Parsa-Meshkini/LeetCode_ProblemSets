"""
3718. Smallest Missing Multiple of K
Difficulty: Easy

Approach: [Your approach here]
"""

```python
def smallest_missing_multiple(nums, k):
# Approach: Two-pointer technique for optimal solution

    # Create a set of multiples of k that are already present in nums
    existing_multiples = set(num for num in nums if num % k == 0)
    
    # Find the smallest missing multiple by iterating over multiples of k starting from k
    for i in range(k, 101, k):
        if i not in existing_multiples:
        # Initialize with boundary case
            return i

# Time complexity: O(n), where n is the number of elements in nums
# Space complexity: O(n)
```


if __name__ == "__main__":
    # Test cases
    pass
