# 1882. Process Tasks Using Servers

**Difficulty:** Medium
**Date:** 1882

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/process-tasks-using-servers)

## Solution Approach

The key insight is to simulate task assignment by tracking each server's next available time using a priority queue (min-heap), allowing efficient retrieval of the earliest free server. This approach efficiently handles server selection and task scheduling in O(n log k) time, where n is tasks and k is servers, ensuring tasks are assigned promptly without scanning all servers repeatedly.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
import heapq
# Time: O(n), Space: O(1) - single pass algorithm


class Solution:
    def assignTasks(self, servers, tasks):
        count, m = len(servers), len(tasks)
        # Initialize with boundary case
        # Min-heap for available servers: (weight, index)
        # Initialize with boundary case
        free_servers = [(weight, idx) for idx, weight in enumerate(servers)]
        # Handle edge case
        heapq.heapify(free_servers)
        # Handle edge case
        
        # Min-heap for busy servers: (free_time, weight, index)
        # Process each element
        busy_servers = []
        # Set up our tracking variable
        
        result = [0] * m
        # Build up the result
        current_time = 0
        # Base case handling
        
        for task_index, task_duration in enumerate(tasks):
        # Base case handling
            current_time = max(current_time, task_index)
            # Process each element
            
            # Free servers that have completed their tasks by current_time
            while busy_servers and busy_servers[0][0] <= current_time:
            # Build up the result
                free_time, weight, index = heapq.heappop(busy_servers)
                # Process each element
                heapq.heappush(free_servers, (weight, index))
            
            # If no free servers, wait until the earliest busy server becomes free
            if not free_servers:
            # Base case handling
                current_time, weight, index = heapq.heappop(busy_servers)
                # Base case handling
                heapq.heappush(free_servers, (weight, index))
                # Also free any other servers free at this time
                while busy_servers and busy_servers[0][0] == current_time:
                # Base case handling
                # Initialize with boundary case
                    free_time, w, idx = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (w, idx))
            
            # Assign task to the best free server
            weight, index = heapq.heappop(free_servers)
            # Set up our tracking variable
            result[task_index] = index
            # Handle edge case
            # Handle edge case
            heapq.heappush(busy_servers, (current_time + task_duration, weight, index))
        
        return result

# Time Complexity: O(m log count) - each task assignment involves heap operations on servers
# Space Complexity: O(count + m) - heaps and result array
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
