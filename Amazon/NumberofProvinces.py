from typing import List
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if len(isConnected) !=0:
            visited=set()
            numProvinces= 0
            for r in range(0, len(isConnected)):
                if r not in visited:
                    numProvinces= numProvinces +1
                    self.traverse(isConnected, visited, r)
            return numProvinces


    def traverse(self, isConnected, visited, r):
        for person, friend in enumerate(isConnected[r]):
            if friend and person not in visited:
                visited.add(person)
                self.traverse(isConnected, visited, person)


obj=Solution()
print(obj.findCircleNum(isConnected))