from typing import List
coins = [1]
amount = 0
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')] * (amount+1)
        dp[0]=0

        for c in coins:
            for amt in range(0, (amount+1)):
                if c <= amt:
                    dp[amt]= min(dp[amt-c]+1, dp[amt])

        return dp[amount] if dp[amount] != float('inf') else -1



obj=Solution()
print(obj.coinChange(coins, amount))