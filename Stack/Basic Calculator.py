import re
s="- (3 + (4 + 5))"
class Solution:
    def calculate(self, s: str) -> int:
        if len(s)==1:
            return s[0].isdigit()
        s.replace(' ', '')
        st = re.split(r'(\D)', s)
        hold=[]
        calSum=0
        opera='+'
        operators=['+', '-']
        for i in st:
            if i !='':
                if i.isdigit():
                    if opera=="+":
                        calSum= calSum+ int(i)
                    elif opera =='-':
                        calSum = calSum - int(i)
                elif i in operators:
                    opera= i
                elif i == '(':
                    hold.append(calSum)
                    hold.append(opera)
                    calSum= 0
                    opera="+"
                elif i ==')':
                    opera=hold.pop()
                    num= hold.pop()
                    if opera =="+":
                        calSum= calSum + num
                    elif opera =='-':
                        calSum = num-calSum
        hold.append(calSum)
        finalCal=0
        ope='+'
        for i in hold:
            if i not in operators:
                if ope=="+":
                    finalCal= finalCal + i
                elif ope=="-":
                    finalCal = finalCal - i
            elif i in operators:
                ope= i


        return finalCal


obj=Solution()
print(obj.calculate(s))