from typing import List
s= "cbaebabacd"
p= "abc"

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = ''.join(sorted(p))
        anagrams = []
        hold = s[:len(p)]
        index=len(p)-1
        while index < len(s):

            if len(hold)==len(p):
                hold=''.join(sorted(hold))
                if hold == p:
                    anagrams.append(index-(len(p)-1))
                index= (index-(len(p)-1)) +1
                hold =''
            elif len(hold) < len(p):
                index = index+1
            if index < len(s):
             hold = hold + s[index]
        return anagrams

obj=Solution()
print(obj.findAnagrams(s, p))
