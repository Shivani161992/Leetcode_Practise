from typing import List

nums = [1, 2, 3, 1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            dp = len(nums) * [0] + [0]
            dp[0] = 0
            dp[1] = nums[0]
            j = 1
            for i in range(2, len(dp)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[j])
                j = j + 1
            return dp[-1]


obj = Solution()
print(obj.rob(nums))
