num= 14
class Solution:
    def numberOfSteps (self, num: int) -> int:
        count= 0
        if num ==0:
            return count
        else :
            while num != 0:
                if num % 2 == 0:
                    num = num / 2
                    count +=1
                elif num % 2 == 1:
                    num = num - 1
                    count += 1

        return count


o=Solution()
y=o.numberOfSteps(num)
print(y)