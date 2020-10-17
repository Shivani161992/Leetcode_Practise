s = "ac"
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 0 or s == s[::-1]:
            return s
        else:
            longest = s[0]
            for i in range(0, len(s)):
                hold = s[i]
                for j in range(i+1, len(s)):

                    hold = hold + s[j]
                    if hold == hold[::-1] and len(hold) > len(longest):
                        longest = hold
            return longest


obj=Solution()
print(obj.longestPalindrome(s))