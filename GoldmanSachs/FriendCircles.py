from typing import List
M=[[1,1,0],
 [1,1,1],
 [0,1,1]]
class Solution:
    def findCircleNum_my(self, M: List[List[int]]) -> int:
        friend_circle=0
        for sp in range(0, len(M)):
            for p in range(0, len(M[0])):
                #check if  its a friend
                if M[sp][p] == 1:
                    friend_circle= friend_circle + 1
                    self.find_friend(sp, M)
        return friend_circle


    def find_friend_my(self, sp, M):
        for p in range(0, len(M[0])):
            if sp==p:
                M[sp][p] = 0
            elif M[sp][p]==1:
                M[sp][p] = 0
                M[p][sp] = 0
                self.find_friend(p, M)
    # another solution using visited

    def findCircleNum(self, M: List[List[int]]) -> int:
        friend_circle=0
        visited=set()
        for sp in range(0, len(M)):
            if sp not in visited:
                friend_circle = friend_circle + 1
                self.find_friend(sp, M, visited)
        return friend_circle


    def find_friend(self, sp, M, visited):
        for person, friend in enumerate(M[sp]):
            if friend == 1 and person not in visited:
                visited.add(person)
                self.find_friend(person, M, visited)









o=Solution()
print(o.findCircleNum(M))
