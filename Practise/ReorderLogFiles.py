from typing import List
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs=[]
        digit_logs=[]
        for log in logs:
            second=log.split(sep=' ')
            if second[1][0].isdigit()== True:
                digit_logs.append(log)
            elif second[1][0].isdigit()== False:
                letter_logs.append(log)
                letter_logs.sort(key=lambda x : (x.split(sep=' ', maxsplit=1)[1], x.split(sep=' ', maxsplit=1)[0]))

        return letter_logs + digit_logs


obj=Solution()
print(obj.reorderLogFiles(logs))
