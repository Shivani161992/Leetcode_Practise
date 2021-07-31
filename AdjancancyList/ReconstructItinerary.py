from typing import List
from collections import defaultdict
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if len(tickets) > 0:
            adjList = defaultdict(list)
            for ticket in tickets:
                departure = ticket[0]
                arrival = ticket[1]
                adjList[departure].append(arrival)
            for adj in adjList:
                adjList[adj].sort()
            reconsItinerary=['JFK']
            self.dfs('JFK', adjList, reconsItinerary)
            return reconsItinerary
    def dfs(self, start, adjList, reconsItinerary):
        if start in adjList:
            getItinerary= adjList[start]
            while len(getItinerary) !=0:
                nextStop = getItinerary.pop(0)
                reconsItinerary.append(nextStop)
                self.dfs(nextStop, adjList, reconsItinerary)
            else:
                return
        else:
            return
obj = Solution()
print(obj.findItinerary(tickets))
