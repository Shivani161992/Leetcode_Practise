num=65
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        power = 0
        su = 0
        while su < num:
            su = 4 ** power
            if su == num:
                return True
            else:
                power = power + 1
        return False

o=Solution()
y=o.isPowerOfFour(num)
print(y)