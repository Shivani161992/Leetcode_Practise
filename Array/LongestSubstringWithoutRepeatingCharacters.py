s="abcabcbb"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(set(s)) == 1:
            return 1
        hold=0
        hold_string=""
        for j in s:
            if j not in hold_string:
                hold_string = hold_string + j
            elif j in hold_string:
                hold=max(hold, len(hold_string))
                indx=hold_string.index(j) + 1
                if(len(hold_string)==indx):
                    hold_string = j
                else:
                    hold_string=hold_string[indx:] + j
        hold=max(hold, len(hold_string))
        return hold



o=Solution()
y=o.lengthOfLongestSubstring(s)
print(y)