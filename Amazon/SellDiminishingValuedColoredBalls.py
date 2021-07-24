from typing import List

inventory = [2,8,4,10,6]
orders = 20

import heapq as h
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        if len(inventory) >1:
            h._heapify_max(inventory)
            profit=0
            while orders >0:
                getball= h.heappop(inventory)
                profit= profit + getball
                if getball-1 != 0:
                    h.heappush(inventory, getball-1)
                h._heapify_max(inventory)
                orders= orders-1

        return profit % (10 ** 9 +7)

obj = Solution()
print(obj.maxProfit(inventory, orders))
