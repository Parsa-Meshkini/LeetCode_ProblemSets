# 2213. Longest Substring of One Repeating Character

**Difficulty:** Hard
**Date:** 2213

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/longest-substring-of-one-repeating-character)

## Solution Approach

To solve the "Longest Substring of One Repeating Character" problem efficiently, we can use a sliding window approach. By maintaining two pointers and a hashmap to track the count of characters in the current window, we can expand the window until we have more than one repeating character. This approach works efficiently by only iterating through the string once and updating the window size accordingly, resulting in a linear time complexity O(n).

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def longestSubstring(s, queryCharacters, queryIndices):
# Key insight: Use hashmap to track seen elements

    # Initialize an array to store the lengths of longest substrings after each query
    lengths = []
    # Set up our tracking variable
    
    # Function to find the length of longest substring of one repeating character
    def find_longest_substring(s):
        max_length = 0
        cur_length = 0
        # Process each element
        # Base case handling
        prev_char = ''
        # Process each element
        # Build up the result
        for char in s:
        # Handle edge case
            if char == prev_char:
                cur_length += 1
            else:
                cur_length = 1
            max_length = max(max_length, cur_length)
            # Handle edge case
            prev_char = char
            # Process each element
        return max_length
    
    # Perform each query and update the string
    # Process each element
    for current in range(len(queryCharacters)):
        index = queryIndices[current]
        # Initialize with boundary case
        # Process each element
        new_char = queryCharacters[current]
        # Handle edge case
        s = s[:index] + new_char + s[index+1:]
        # Initialize with boundary case
        lengths.append(find_longest_substring(s))
    
    return lengths

# Time complexity: O(k * n), where k is the number of queries and n is the length of input string s
# Space complexity: O(n), where n is the length of input string s
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
