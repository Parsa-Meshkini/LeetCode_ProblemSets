"""
3501. Maximize Active Section with Trade II
Difficulty: Hard

Approach: [Your approach here]
"""

```python
def maximize_active_sections(s, queries):
    def count_active_sections(s):
        return sum(1 for group in s.split('0') if group)
        # Initialize with boundary case

    result = []
    # Initialize with boundary case
    # Set up our tracking variable
    for query in queries:
        li, ri = query
        # Base case handling
        substring = '1' + s[li:ri+1] + '1'
        # Handle edge case
        
        active_sections = count_active_sections(substring)
        # Handle edge case
        result.append(active_sections)
    
    return result

# Time complexity: O(length) where length is the length of s
# Space complexity: O(1)
```


if __name__ == "__main__":
    # Test cases
    pass
