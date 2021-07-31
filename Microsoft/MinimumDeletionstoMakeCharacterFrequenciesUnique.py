from collections import Counter, defaultdict
s="accdcdadddbaadbc"
class Solution:
    def minDeletions(self, s: str) -> int:
        if len(s)==0:
            return 0
        else:
            minDel=0
            getFreq= Counter(s).most_common()
            storefreq= set()
            prev=None
            for freq in getFreq:
                storefreq.add(freq[1])

            for f in getFreq:
                if f[1] !=prev:
                    prev= f[1]
                elif f[1] ==prev:
                    for j in range(f[1]-1, -1, -1):
                        minDel= minDel+ 1
                        if j not in storefreq and j !=0:
                            storefreq.add(j)
                            break
            return minDel

obj=Solution()
print(obj.minDeletions(s))
