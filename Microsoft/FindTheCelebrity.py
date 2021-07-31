
n=3
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate=0
        for i in range(1, n):
            if knows(candidate, i) == True:
                candidate= i

        for i in range(0, n):
            if candidate !=i and (knows(candidate, i)==True or knows(i, candidate)==False):
                return -1
        return candidate
obj = Solution()
print(obj.findCelebrity(n))
