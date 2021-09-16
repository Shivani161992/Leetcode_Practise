from typing import List
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if len(logs)==0:
            return []
        else:
            output=[]
            digitLogs=[]
            letterLogs=[]
            for log in logs:
                logType=log.split(' ', 1)
                if logType[1][0].isdigit():
                    digitLogs.append(log)
                else:
                    letterLogs.append(log)
                    letterLogs.sort(key=lambda x: (x.split(' ', 1)[1], x.split(' ', 1)[0]))
            return letterLogs+digitLogs
obj=Solution()
print(obj.reorderLogFiles(logs))
