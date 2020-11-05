from typing import List
n=5
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        elif numRows > 2:
            tri=[[1], [1,1]]
            for i in range(2, numRows):
                get_row= tri[i-1]
                group=[1]
                for j in range(0, len(get_row)-1):
                    psum= get_row[j] + get_row[j+1]
                    group.append(psum)
                group.append(1)
                tri.append(group.copy())

            return tri

obj=Solution()
print( obj.generate(n))