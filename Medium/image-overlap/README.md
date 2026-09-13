# 835. Image Overlap

**Difficulty:** Medium
**Date:** 835

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/image-overlap)

## Solution Approach

The key insight in solving the "Image Overlap" problem is to consider each pair of corresponding pixels in the two images and calculate their relative offset positions. By leveraging this offset information, we can efficiently determine the maximum number of overlapping pixels by using a hashmap to store the frequency of different offsets. This approach works efficiently because it reduces the problem to a simple frequency counting task, optimizing the computation and space complexity.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
def largestOverlap(img1, img2):
# Time: O(n), Space: O(1) - single pass algorithm

# Key insight: Use hashmap to track seen elements

    count = len(img1)
    # Build up the result
    # Process each element
    max_overlap = 0
    
    # Calculate all possible translations
    translations = [(current, end) for current in range(-count+1, count) for end in range(-count+1, count)]
    # Build up the result
    # Initialize with boundary case
    
    # Check overlap for each translation
    for dx, dy in translations:
    # Process each element
    # Build up the result
        overlap = 0
        # Set up our tracking variable
        for current in range(max(0, -dx), min(count, count-dx)):
        # Base case handling
        # Initialize with boundary case
            for end in range(max(0, -dy), min(count, count-dy)):
            # Initialize with boundary case
                overlap += img1[current+dx][end+dy] & img2[current][end]
        max_overlap = max(max_overlap, overlap)
        # Base case handling
        # Build up the result
    
    return max_overlap
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
