class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        n = len(prices)

        base = 0
        for i in range(n):
            base += prices[i] * strategy[i]

        half = k // 2

        leftGain = [0] * n
        rightGain = [0] * n

        for i in range(n):

            # make strategy[i] = 0
            leftGain[i] = -strategy[i] * prices[i]

            # make strategy[i] = 1
            rightGain[i] = prices[i] - strategy[i] * prices[i]

        gain = 0

        for i in range(half):
            gain += leftGain[i]

        for i in range(half, k):
            gain += rightGain[i]

        best = max(0, gain)

        for start in range(1, n - k + 1):

            gain -= leftGain[start - 1]
            gain += leftGain[start + half - 1]

            gain -= rightGain[start + half - 1]
            gain += rightGain[start + k - 1]

            best = max(best, gain)

        return base + best