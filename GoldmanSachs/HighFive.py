items= [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
from typing import List
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x: (x[0], -x[1]))
        student=None
        avg_sum=0
        count=0
        out=[]
        for item in items:
            if student == None or student == item[0]:
                count = count + 1
                if count <= 5:
                    student = item[0]
                    avg_sum= avg_sum + item[1]

                elif count > 5:
                    avg = avg_sum / 5
                    avg_sum = item[1]
                    count = 1
                    student = item[0] if item[0] != student else student
                    out.append([student, avg])
            elif student != None or student != items[0]:
                    avg= avg_sum/count
                    avg_sum=items[1]
                    count=1
                    student= items[0]
                    out.append([student, avg])




        return out

obj=Solution()
print(obj.highFive(items))


