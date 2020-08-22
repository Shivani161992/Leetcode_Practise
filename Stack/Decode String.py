s = "abc3[cd]xyz"

class Solution:
    def decodeString(self, s: str) -> str:
        digit=''
        hold=''
        string=''
        stack = []
        for j, i in enumerate(s):
            if i.isdigit()==True:

                if digit == '':
                    digit=i
                elif digit !='':
                    if s[j-1].isdigit()==True:
                        digit= digit + i
                    elif s[j-1].isdigit()==False:
                        stack.append(digit)
                        stack.append(hold)
                        digit = i
                        hold=''
            elif i == ']':
                if len(stack)==0:
                    string = string + str(int(digit) * hold)
                    hold=''
                    digit=''
                elif len(stack) !=0:
                    hold=int(digit) * hold
                    hold=stack.pop()+hold
                    digit=stack.pop()

            elif i != '[':
                if digit == '':
                    string = string +i
                else:
                    hold=hold+i

        string = string + hold
        return string


obj=Solution()
print(obj.decodeString(s))