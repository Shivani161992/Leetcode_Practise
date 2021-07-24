s = "42"
import re


class Solution:
    def calculate(self, s: str) -> int:
        st= re.split(r'(\D)', s)
        if len(st) == 1:
            return st[0]
        else:

            stack = []
            prio1 = ["*", "/"]
            prio2 = ["+", "-"]
            inPrio = False
            ops = None
            for exp in st:
                if exp.isdigit():
                    if inPrio == True:
                        inPrio = False
                        eval = 0
                        if ops == "*":
                            eval = stack.pop() * int(exp)
                        elif ops == "/":
                            eval = stack.pop() // int(exp)
                        stack.append(eval)
                    else:
                        stack.append(int(exp))
                elif exp in prio2:
                    stack.append(exp)
                elif exp in prio1:
                    inPrio = True
                    ops = exp


            prev = None
            ops = None
            while stack:
                if prev == None:
                    prev = stack.pop(0)
                else:
                    if ops == None:
                        ops = stack.pop(0)
                    if ops == "+":
                        prev=stack.pop(0) + prev
                    elif ops == "-":
                        prev=prev- stack.pop(0)
                    ops=None
            return prev


obj = Solution()
print(obj.calculate(s))
