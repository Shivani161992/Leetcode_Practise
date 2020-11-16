s="cacacb"
from collections import defaultdict
class Solution:
    def lastSubstring(self, s: str) -> str:
        max_letter= max(s)
        if s.count(max_letter) == len(s):
            return s
        all_idxs= [i for i in range(len(s)) if s[i]==max_letter]
        all_substring= [s[i:] for i in all_idxs]
        all_substring.sort()
        return all_substring[-1]

    def lastSubstring2(self, s: str) -> str:
        i=0 # first index of the string
        j=1 # j is always i+1. second index of the string
        k=0 # k is just next elemenst after first and second string
        n=len(s)
        while j + k < n:
            a=s[i+k]
            b=s[j+k]
            if s[i+k]==s[j+k]:
                k = k+1
            elif s[i+k] > s[j+k]:
                j=j+k+1
                k=0
            elif s[i+k] < s[j+k]:
                i= j
                j=i+1
                k=0
        return s[i:]


obj=Solution()
print(obj.lastSubstring2(s))