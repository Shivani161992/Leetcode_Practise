items= [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
from typing import List
from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        avg_score = []
        if len(items)==0:
            return avg_score
        #create default dictionary
        group_scores= defaultdict(list)
        #collect scores in a default dictionary on the basis of their id
        for item in items:
            group_scores[item[0]].append(item[1])
        for stud in group_scores:
            scores= group_scores[stud]
            #sort to get highest marks
            scores.sort(reverse=True)

            avg= sum(scores[:5]) // len(scores[:5])
            avg_score.append([stud, avg])


        return avg_score

obj=Solution()
print(obj.highFive(items))


