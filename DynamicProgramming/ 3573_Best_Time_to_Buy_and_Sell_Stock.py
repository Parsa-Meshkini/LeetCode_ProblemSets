class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        NEG = float('-inf')

        # free[t]  -> no open transaction
        # long[t]  -> holding normal buy
        # short[t] -> holding short sell

        free = [NEG] * (k + 1)
        long = [NEG] * (k + 1)
        short = [NEG] * (k + 1)

        free[0] = 0

        for price in prices:

            new_free = free[:]
            new_long = long[:]
            new_short = short[:]

            for t in range(k + 1):

                # open normal transaction
                new_long[t] = max(
                    new_long[t],
                    free[t] - price
                )

                # open short transaction
                new_short[t] = max(
                    new_short[t],
                    free[t] + price
                )

                # close transactions
                if t < k:

                    # close normal transaction
                    new_free[t + 1] = max(
                        new_free[t + 1],
                        long[t] + price
                    )

                    # close short transaction
                    new_free[t + 1] = max(
                        new_free[t + 1],
                        short[t] - price
                    )

            free = new_free
            long = new_long
            short = new_short

        return max(free)