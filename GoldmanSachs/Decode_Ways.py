s = "0"
class Solution:
    def numDecodings(self, s: str) -> int:
        # just check if the numbers are valid or not
        # whether the current number is greater than 0 or current + prev number lies between 10-26

        dp= [0] * (len(s) +1)
        dp[0] = 1

        dp[1] = 0 if s[0]=='0' else 1
        for i in range(2, (len(s)+1)):

            if int(s[i-1]) > 0:
                dp[i] = dp[i] + dp[i - 1]
            if 10<= int(s[i-2:i]) <=26:
                dp[i] = dp[i] + dp[i - 2]
        return dp[len(s)]




obj=Solution()
print(obj.numDecodings(s))
