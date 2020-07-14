S="abbaca"
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = [S[0]]
        for i in range(1, len(S)):
            size=len(stack)
            if size==0 or S[i] != stack[size - 1]:
                stack.append(S[i])
            elif S[i] == stack[size - 1]:
                stack.pop()
        return ''.join(stack)


o=Solution()
y=o.removeDuplicates(S)
print(y)