s = "LEETCODE"
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        count = len(s)
        for i in range(0, len(s)):
            hold = s[i]
            for j in range(i + 1, len(s)):
                hold = hold + s[j]
                x = [i for i in set(hold) if hold.count(i) == 1]
                count = count + len(x)
        return count


o=Solution()
y=o.uniqueLetterString(s)
print(y)