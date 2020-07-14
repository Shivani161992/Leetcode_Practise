from typing import List
left = 1
right = 10000
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range(left, right + 1):
            dig=i
            iszero=0
            while dig !=0:
                dig, div=divmod(dig, 10)
                if(div!=0):
                    if i%div != 0:
                        iszero = 1
                        break
                elif(div==0):
                    iszero=1
                    break
            if(iszero==0):
                l.append(i)
        return l

o=Solution()
y=o.selfDividingNumbers(left, right)
print(y)