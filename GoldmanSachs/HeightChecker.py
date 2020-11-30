from typing import List
heights = [1,1,4,2,1,3]
class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        sorted_heights=sorted(heights)
        min_student=0
        if sorted_heights == heights:
            return min_student

        for i, h in enumerate(heights):
            if h != sorted_heights[i]:
                min_student= min_student + 1
        return min_student

obj=Solution()
print(obj.heightChecker(heights))
