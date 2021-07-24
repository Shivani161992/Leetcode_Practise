s = "10"
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)==0:
            return 0
        else:
            dp=[0] * (len(s)+1)
            dp[0]=1
            dp[1]= 0 if s[0]=='0' else 1
            for i in range(2, len(s)+1):
                if int(s[i-1]) >0:
                    dp[i]=dp[i-1]
                if int(s[i-2]) >0:
                    if 10 <= int(s[i-2]+s[i-1]) <= 26:
                        dp[i] = dp[i - 2] + dp[i]
            return dp[len(s)]



obj=Solution()
print(obj.numDecodings(s))
