s= "{[]}"
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[s[0]]
        hold=""
        valid=["()", "[]", "{}"]
        index=1
        while len(stack) != 0 and index < len(s) :
            get=stack[len(stack)-1]
            curr=s[index]
            hold= get + curr
            if hold in valid:
                stack.pop()
                index= index + 1
                if len(stack)==0 and index < len(s):
                    stack.append(s[index])
                    index= index + 1
            elif hold not in valid:
                stack.append(curr)
                index = index + 1

        if len(stack) != 0 :
            return False
        else:
            return True

obj= Solution()
print(obj.isValid(s))