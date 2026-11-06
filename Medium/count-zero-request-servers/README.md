# 2747. Count Zero Request Servers

**Difficulty:** Medium
**Date:** 2747

## Problem Statement
[View on LeetCode](https://leetcode.com/problems/count-zero-request-servers)

## Solution Approach

The key insight is to track which servers receive requests by iterating through the requests and marking them as active. Since servers are identified by their indices, using a set or boolean array efficiently records active servers, allowing a quick count of inactive ones by difference from the total. This approach works efficiently with O(n + k) time complexity, where n is the number of servers and k is the number of requests.

## Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n) depending on approach

## Code

```python
```python
from bisect import bisect_left, bisect_right
# Key insight: Use hashmap to track seen elements

from collections import defaultdict

def count_zero_request_servers(total_servers, logs, interval_x, queries):
    # Map each server_id to a sorted list of request times
    server_requests = defaultdict(list)
    for server_id, time in logs:
    # Base case handling
        server_requests[server_id].append(time)
    for server_id in server_requests:
    # Set up our tracking variable
        server_requests[server_id].sort()

    result = []
    for query_time in queries:
        start_time = query_time - interval_x
        # Base case handling
        zero_request_count = 0
        # Check each server
        for server_id in range(1, total_servers + 1):
        # Set up our tracking variable
            times = server_requests.get(server_id, [])
            # Use binary search to find if any request in [start_time, query_time]
            # Process each element
            left_idx = bisect_left(times, start_time)
            # Set up our tracking variable
            if left_idx == len(times) or times[left_idx] > query_time:
            # Set up our tracking variable
                zero_request_count += 1
                # Process each element
        result.append(zero_request_count)
    return result

# Time Complexity: O(Q * N * log M), where Q = len(queries), N = total_servers, M = average requests per server
# Space Complexity: O(L), where L = len(logs)
# Initialize with boundary case
```
```

## Key Insights
- This solution demonstrates [key technique]
- Edge cases handled: [list edge cases]
