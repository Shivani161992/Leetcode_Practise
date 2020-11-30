height = [0,1,0,2,1,0,1,3,2,1,2,1]
from typing import List
class Solution:
    def trap_bruteforce(self, height: List[int]) -> int:
        water = 0
        if len(height) < 2:
            return water
        for i in range(0, len(height)):
            leftmax=max(height[:i+1])
            rightmax=max(height[i:])
            minheight_build= min(leftmax, rightmax)
            water= water + (minheight_build - height[i])
        return water

    #hold all
    def trap_dynamic_programming(self, height: List[int]) -> int:
        water=0
        left_max = (len(height)) * [None]
        right_max = (len(height)) * [None]
        if len(height) < 2:
            return water

        #for left max
        for i in range(0, len(height)):
            if i == 0:
                left_max[i] = height[i]
            elif i !=0:
                left_max[i] = max(left_max[i-1], height[i])
        #for right max
        for j in range(len(height)-1, -1, -1):
            if j == len(height)-1:
                right_max[j]= height[j]
            elif j != len(height)-1:
                right_max[j] = max(height[j], right_max[j+1])

        #find maximum water
        for i in range(0, len(height)):
            min_building=min(left_max[i], right_max[i])
            water= water + (min_building - height[i])
        return water

    # calculate all in one go
    def trap_dp(self, height: List[int]) -> int:
        water = 0
        if len(height) < 2:
            return water
        l= 0
        h= len(height) -1
        lmax= height[l]
        rmax= height[h]

        while l != h:
            if lmax <= rmax:
                build= lmax - height[l]
                l = l + 1
                lmax= max(lmax, height[l])
            elif lmax > rmax:
                build= rmax - height[h]
                h = h - 1
                rmax= max(rmax, height[h])
            water= water + build
        return water





obj=Solution()
print(obj.trap_dp(height))