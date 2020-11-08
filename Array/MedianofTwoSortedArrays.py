nums1 = [1,2]
nums2 = [3, 4]
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # to improve the time complexity we are not going to merge the two arrays and sort it to find the median.
        # rather then we are going to find the median without merging the arrays.
        # time complexity will be O(min(nums1, nums2)
        # first find which array is the smallest and put it in nums1

        if len(nums1) > len(nums2):
            temp= nums1
            nums1= nums2
            nums2= temp

        low=0
        high= len(nums1)
        total = (len(nums1)) + (len(nums2))

        while low <= high:
            #find partition of x
            #formula to find partition y
            # partition_x + partition_y = x + y + 1 // 2
            pnums1 = (low + high) // 2 #(mid of nums1)
            pnums2 =(total + 1) // 2 - pnums1

            # check if left part of nums1 is less than right part of nums2
            # check if left part of nums2 is less than right part of nums1
            # see if partition is reaching extreme left or extreme right
            #for nums1
            left_maxnums1 = float('-inf') if pnums1 == 0 else nums1[pnums1 - 1]
            right_minnums1 = float('inf') if pnums1 == len(nums1) else nums1[pnums1]

            #for nums2
            left_maxnums2 = float('-inf') if pnums2 == 0 else nums2[pnums2 - 1]
            right_minnums2 = float('inf') if pnums2 == len(nums2) else nums2[pnums2]

            if left_maxnums1 <= right_minnums2 and left_maxnums2 <= right_minnums1:
                if total % 2 == 0:
                    avg = (max(left_maxnums1, left_maxnums2)  + min(right_minnums1, right_minnums2) )/ 2.0
                    return avg
                else:
                    return max(left_maxnums1, left_maxnums2)
            elif left_maxnums1 > right_minnums2 :
                #move towards left side of nums1
                high = pnums1 - 1
            elif left_maxnums2 > right_minnums1:
                # move towards left side of nums1
                low =  pnums1 + 1

obj=Solution()
print(obj.findMedianSortedArrays(nums1, nums2))
