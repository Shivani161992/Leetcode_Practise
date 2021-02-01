s = "(a(b(c)d)"
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if len(s)==0:
            return s
        else:
            store_paren=[]
            store_idx=[]
            hold=''
            hold_idx=0
            paren='()'
            for idx, val in enumerate(s):
                if val=='(':
                    if hold !='':
                        store_paren.append(hold)
                        store_idx.append(hold_idx)

                    hold = val
                    hold_idx = idx
                elif val==')':
                    if hold == '':
                        store_paren.append(val)
                        store_idx.append(idx)
                    elif hold !='':

                        hold = hold + val
                        if hold == paren and len(store_paren) !=0 and store_paren[-1]=='(' :
                            hold = store_paren.pop()
                            hold_idx = store_idx.pop()
                        else:
                            hold = ''
                            hold_idx = 0
            if hold != '':
                store_paren.append(hold)
                store_idx.append(hold_idx)

            output=''
            for i in range(0, len(s)):
                if i not in store_idx:
                    output= output + s[i]
            return output
obj=Solution()
print(obj.minRemoveToMakeValid(s))
