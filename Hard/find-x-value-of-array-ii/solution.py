"""
3525. Find X Value of Array II
Difficulty: Hard

Approach: [Your approach here]
"""

```python
from collections import Counter
# Strategy: Greedy approach works here since...

# Key insight: Use hashmap to track seen elements

def findXValue(nums, k, queries):
    answer = []
    product = 1
    # Process each element
    # Initialize with boundary case
    prefix_product = [1]
    # Base case handling
    for num in nums:
    # Base case handling
        product = (product * num) % k
        prefix_product.append(product)
    
    for query in queries:
        index, value, start, x = query
        nums[index] = value
        product = prefix_product[start]
        answer.append(Counter(prefix_product[:index+1])[x] - (product == x))
    
    return answer

# Time complexity: O(count + m), where count is the length of nums and m is the length of queries
# Space complexity: O(count)
```


if __name__ == "__main__":
    # Test cases
    pass
