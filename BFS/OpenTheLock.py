from typing import List
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadendset = set(deadends)

        start = "0000"
        if start in deadendset:
            return -1
        elif start == target:
            return 0
        else:
            move = -1
            visited = set()
            queue = [start]
            visited.add(start)
            while queue:
                print(queue)
                groupSize = len(queue)
                move = move + 1
                for i in range(0, groupSize):
                    code = queue.pop(0)
                    for j in range(0, len(code)):

                        digit1 = (int(code[j]) + 1) % 10
                        code1 = code[:j] + str(digit1) + code[j + 1:]
                        digit2 = (int(code[j]) - 1) % 10
                        code2 = code[:j] + str(digit2) + code[j + 1:]

                        if code1 == target or code2 == target:
                            return move + 1
                        if code1 not in visited and code1 not in deadendset:
                            queue.append(code1)
                            visited.add(code1)
                        if code2 not in visited and code2 not in deadendset:
                            queue.append(code2)
                            visited.add(code2)

            return -1

obj= Solution()
print(obj.openLock(deadends, target))


