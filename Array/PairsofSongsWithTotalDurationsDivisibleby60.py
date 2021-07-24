from typing import List
from collections import defaultdict

time = [30,20,150,100,40]


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if len(time) < 2:
            return 0
        else:
            pairs = set()
            maxTime = 0
            # create default dict
            timedict = defaultdict(list)
            for idx, t in enumerate(time):
                timedict[t].append(idx)
                maxTime = max(maxTime, t)
            # find pairs

            for tim in timedict:
                n = 1
                while ((60 * n) - tim) <= maxTime:
                    diff = (60 * n) - tim
                    if diff in timedict:
                        getfirst = timedict[tim]
                        getSecond = timedict[diff]
                        for f in getfirst:
                            for s in getSecond:
                                if f != s:
                                    pair = (f, s) if f <= s else (s, f)
                                    pairs.add(pair)
                    n = n + 1
            return len(pairs)


obj = Solution()
print(obj.numPairsDivisibleBy60(time))
