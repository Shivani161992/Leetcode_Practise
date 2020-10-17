from typing import List
costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        minimum_cost=0
        costs.sort(key=lambda x: (x[0]-x[1]))
        count=0
        for i in range(0, len(costs)):
            count= count + 1
            minimum_cost= (minimum_cost+ costs[i][0]) if count <= (len(costs)/2) else (minimum_cost + costs[i][1])

        return minimum_cost





obj= Solution()
print(obj.twoCitySchedCost(costs))
