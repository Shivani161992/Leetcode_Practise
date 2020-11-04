from typing import List
s= ["h","e","l","l","o"]
class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) ==0:
            return s
        else:
            low = 0
            high = len(s)-1
            while low < high:
                temp = s[high]
                s[high]= s[low]
                s[low]= temp

                low= low+1
                high= high-1



obj= Solution()
(obj.reverseString(s))