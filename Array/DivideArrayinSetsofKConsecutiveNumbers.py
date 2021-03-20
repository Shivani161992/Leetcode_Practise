from typing import List
from collections import Counter

nums = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
k = 3


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        dict = Counter(nums)
        elements = list(dict.keys())
        elements.sort()
        divisible = False
        count = 0
        prev = ''
        while len(elements) != 0:
            divisible = False
            for e in elements:
                if dict[e] > 0:
                    if prev == '':
                        prev = e
                        dict[e] = dict[e] - 1
                        count = count + 1
                    else:
                        if e - prev == 1:
                            dict[e] = dict[e] - 1
                            count = count + 1
                            prev = e
                        else:
                            return divisible
                    if count == k:
                        count = 0
                        prev = ''
                        divisible== True
                        break

        return divisible




        print(dict)


obj = Solution()
print(obj.isPossibleDivide(nums, k))
