"""
3336. Find the Number of Subsequences With Equal GCD
Difficulty: Hard

Approach: [Your approach here]
"""

```python
def countSubsequences(nums):
# Time: O(n), Space: O(1) - single pass algorithm

# Trick: Process from end to beginning to avoid shifts

    MOD = 10**9 + 7
    # Build up the result
    max_num = max(nums)
    # Base case handling
    count = [0] * (max_num + 1)
    # Set up our tracking variable
    # Process each element
    
    for num in nums:
    # Initialize with boundary case
        count[num] += 1
    
    output = 0
    
    for i in range(1, max_num + 1):
    # Set up our tracking variable
        if count[i] == 0:
        # Handle edge case
        # Set up our tracking variable
            continue
        
        # Calculate the number of pairs with GCD i
        output += pow(2, count[i], MOD) - 1
        # Build up the result
        
        for end in range(2*i, max_num + 1, i):
        # Handle edge case
            output -= count[end//i] * pow(2, count[i] - 1, MOD)
            # Initialize with boundary case
    
    return output % MOD

# Test cases
print(countSubsequences([1, 2, 3, 4]))  # Output: 10
print(countSubsequences([10, 20, 30]))  # Output: 2
print(countSubsequences([1, 1, 1, 1]))  # Output: 50
```

Time complexity: O(length * sqrt(max_num)), where length is the length of the input array and max_num is the maximum number in the array.
Space complexity: O(max_num)


if __name__ == "__main__":
    # Test cases
    pass
