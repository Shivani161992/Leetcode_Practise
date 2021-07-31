from typing import List
nums = [0, -1]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            longestConsecutive=0
            hashSet=set()
            for n in nums:
                hashSet.add(n)
            numsList = list(hashSet)
            numsList.sort()
            i=0
            while i < len(numsList):
                getMin=numsList[i]
                hashSet.remove(getMin)
                localLongCons=1
                num=getMin
                for j in range(len(hashSet)):
                    num= num +1
                    if num in hashSet:
                        localLongCons = localLongCons +1
                        hashSet.remove(num)
                        i= i+1
                    else:
                        break
                longestConsecutive = max(longestConsecutive, localLongCons)
                i=i+1
            return longestConsecutive

obj=Solution()
print(obj.longestConsecutive(nums))
