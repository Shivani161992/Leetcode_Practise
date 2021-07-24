import re
s="(1+(4+5+2)-3)+(6+8)"
class Solution:
    def calculate(self, s: str) -> int:
        s.replace(' ', '')
        st = re.split(r'(\D)', s)
        if len(st)==1:
            return s[0]
        else:
            cal=0
            stack=[]
            for  i in st:
                print()








obj=Solution()
print(obj.calculate(s))