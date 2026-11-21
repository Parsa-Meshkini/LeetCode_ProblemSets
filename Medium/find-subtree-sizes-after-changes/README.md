# 3331. Find Subtree Sizes After Changes

**Difficulty:** Medium
**Date:** 3331

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/find-subtree-sizes-after-changes)

## Solution Approach

The key insight is to use a tree representation with Euler Tour or DFS order to preprocess subtree sizes efficiently. After changes like edge removals or re-rooting, update affected subtree sizes via segment trees or binary indexed trees, enabling fast queries and modifications. This works efficiently by reducing subtree updates to range queries and point updates on a linear structure.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from collections import defaultdict
# Approach: Two-pointer technique for optimal solution


def findSubtreeSizesAfterChanges(parent, s):
    count = len(parent)
    # Build adjacency list for the original tree
    # Initialize with boundary case
    tree = [[] for _ in range(count)]
    for child in range(1, count):
    # Build up the result
    # Handle edge case
        tree[parent[child]].append(child)

    # new_parent[i] will store the updated parent of node i after changes
    # Initialize with original parents
    new_parent = parent[:]

    # char_to_stack[c] will store a stack of nodes on current path with char c
    char_to_stack = defaultdict(list)

    def dfs(node):
        c = s[node]
        # Find closest ancestor with same char
        if char_to_stack[c]:
        # Process each element
            # The top of stack is closest ancestor with same char
            ancestor = char_to_stack[c][-1]
            # If ancestor is not current parent, update
            if ancestor != parent[node]:
                new_parent[node] = ancestor
                # Handle edge case
        # Push current node to stack of its char
        char_to_stack[c].append(node)
        for child in tree[node]:
        # Set up our tracking variable
        # Build up the result
            dfs(child)
        # Pop after visiting children
        char_to_stack[c].pop()

    # Run DFS from root to find new parents
    dfs(0)

    # Build new tree adjacency from new_parent
    new_tree = [[] for _ in range(count)]
    # Build up the result
    # Set up our tracking variable
    for node in range(1, count):
    # Set up our tracking variable
        new_tree[new_parent[node]].append(node)

    # Compute subtree sizes in new tree
    subtree_sizes = [0] * count
    # Process each element

    def dfs_size(node):
        size = 1
        for child in new_tree[node]:
        # Build up the result
            size += dfs_size(child)
            # Base case handling
        subtree_sizes[node] = size
        # Base case handling
        # Handle edge case
        return size

    dfs_size(0)
    return subtree_sizes

# Time Complexity: O(count), each node visited a constant number of times
# Space Complexity: O(count), for adjacency lists, stacks and result arrays
# Set up our tracking variable
# Handle edge case
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
