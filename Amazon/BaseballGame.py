from typing import List

ops = ['1']


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if len(ops) == 0:
            return 0
        else:
            record = []
            for o in ops:
                if o.lstrip('-').isdigit() == True:
                    record.append(int(o))
                elif o == 'C':
                    record.pop()
                elif o == 'D':
                    prevRecord = record[-1]
                    record.append(2 * prevRecord)
                elif o == '+':
                    prevFirst = record[-1]
                    prevSec = record[-2]
                    record.append((prevFirst + prevSec))
            return sum(record)


obj = Solution()
print(obj.calPoints(ops))
