from typing import List
from collections import Counter

arr = [4, 3, 1, 1, 3, 3, 2]
k = 3


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arrdict = dict()
        for a in arr:
            if a in arrdict:
                arrdict[a] = arrdict[a] + 1
            else:
                arrdict[a] = 1
        freq = dict(sorted(arrdict.items(), key=lambda item: item[1]))
        while k > 0 and len(freq) > 0:
            for f in freq:
                count = freq[f]
                if count <= k:
                    k = k - count
                    del freq[f]
                else:
                    freq[f]= freq[f]-k
                    k = 0
                break
        return len(freq)


obj = Solution()
print(obj.findLeastNumOfUniqueInts(arr, k))
