from typing import List
s = "leetcode"
wordDict = ["leet", "code"]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                print(dp[j])
                print(s[j:i])
                x=dp[j]
                y=s[j:i]
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]

obj=Solution()
print(obj.wordBreak(s, wordDict))
