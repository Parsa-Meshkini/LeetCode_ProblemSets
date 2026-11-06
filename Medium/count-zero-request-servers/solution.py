"""
2747. Count Zero Request Servers
Difficulty: Medium

Approach: [Your approach here]
"""

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


if __name__ == "__main__":
    # Test cases
    pass
