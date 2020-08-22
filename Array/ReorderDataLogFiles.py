from typing import List
logs = ["dig1 8 1 5 1","let2 art can","dig2 3 6","let2 own kit dig","let3 art zero", "let1 art can"]
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        hold_dig=[]
        hold_let=[]
        for log in logs:
            hold=log.split(sep=" ", maxsplit=1)
            if hold[1][0].isdigit() == True:
                hold_dig.append(log)
            else:
                hold_let.append(log)
                hold_let.sort(key=lambda x: (x.split(sep=" ", maxsplit=1)[1], x.split(sep=" ", maxsplit=1)[0]))

        return hold_let + hold_dig

obj=Solution()
print(obj.reorderLogFiles(logs))