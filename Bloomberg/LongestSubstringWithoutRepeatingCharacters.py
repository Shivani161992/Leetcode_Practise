s = "bbbb"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " " or len(s) == 1:
            return 1
        max_size=0
        hold=''
        index = 0
        while index < len(s):
            if s[index] not in hold:
                hold= hold + s[index]
                index= index + 1
            elif s[index] in hold:
                max_size=max(len(hold), max_size)
                index= index - len(hold) + 1
                hold= ""

        max_size = max(len(hold), max_size)
        return max_size


obj=Solution()
print(obj.lengthOfLongestSubstring(s))
