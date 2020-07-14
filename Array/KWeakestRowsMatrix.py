from typing import List
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic={}
        for i in range(0, len(mat)):
            dic[i]=sum(mat[i])
        return sorted(dic, key=dic.get)[:k]


o=Solution()
y=o.kWeakestRows(mat, k)
print(y)