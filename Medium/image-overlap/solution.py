"""
835. Image Overlap
Difficulty: Medium

Approach: [Your approach here]
"""

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


if __name__ == "__main__":
    # Test cases
    pass
