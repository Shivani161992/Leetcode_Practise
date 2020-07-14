from collections import Counter
s="Aabb"
class Solution:
    def frequencySort(self, s: str) -> str:
        x=Counter(s).most_common()
        hold=''
        for i in x:
            hold=hold + (i[0]*i[1])

        return hold

o=Solution()
y=o.frequencySort(s)
print(y)