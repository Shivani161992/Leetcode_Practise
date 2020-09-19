from typing import List
prices=[7,1,5,3,6,4]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0

        if len(prices) == 0 or len(prices) == 1:
            return max_profit
        min_day = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_day:
                min_day = prices[i]

            else:
                min= prices[i]-min_day
                max_profit= max(max_profit, prices[i]-min_day)

        return max_profit


o=Solution()
y=o.maxProfit(prices)
print(y)