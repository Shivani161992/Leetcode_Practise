from typing import List
A=[[1,1,0],[1,0,1],[0,0,0]]
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        A=[i[::-1] for i in A]
        B=[]
        for i in A:
            z =[1 if x == 0 else 0 for x in i]
            B.append(z)

        return B

o=Solution()
y=o.flipAndInvertImage(A)
print(y)