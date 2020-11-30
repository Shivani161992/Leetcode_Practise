prices= [7,1,5,3,6,4]
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        day_price= prices[0]
        for p in range(1, len(prices)):
            if prices[p] < day_price:
                day_price = prices[p]
            elif prices[p] > day_price:
                diff = (prices[p]-day_price)
                max_profit= max(max_profit, diff)
        return max_profit



obj=Solution()
print(obj.maxProfit(prices))