import string

s = "d"
from string import ascii_lowercase
class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) >0:
            if len(s)==1:
                if s[0]=='?':
                    return 'a'
                else:
                    return s
            hold=[]
            for i in range(0, len(s)):
                if s[i] =='?':
                    for l in ascii_lowercase:
                        if i ==0:
                            if s[i+1] != l:
                                hold.append(l)
                                break
                        elif i == len(s)-1:
                            if hold[-1] != l:
                                hold.append(l)
                                break
                        else:
                            if hold[-1] != l and s[i+1] != l:
                                hold.append(l)
                                break
                else:
                    hold.append(s[i])

            output=''
            for h in hold:
                output= output + h

            return output


obj = Solution()
print(obj.modifyString(s))

