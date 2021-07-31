from typing import List
s = "aabaa"
cost = [1,2,3,4,1]
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        prev=s[0]
        maxCost=cost[0]
        letterSum=cost[0]
        minCost=0
        for i in range(1, len(s)):
            if s[i] !=prev:
                prev=s[i]
                minCost = minCost + (letterSum - maxCost)
                maxCost=cost[i]
                letterSum=cost[i]
            elif s[i]== prev:
                maxCost = max(maxCost, cost[i])
                letterSum = letterSum + cost[i]
        minCost = minCost + (letterSum - maxCost)
        return minCost


obj=Solution()
print(obj.minCost(s, cost))


