num=28
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        x=[i for i in range(1, num) if num%i==0]
        if(sum(x)==num):
            return True
        else:
            return False

o=Solution()
y=o.checkPerfectNumber(num)
print(y)