s = "pbbcggttciiippooaais"
k = 2
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = list(s[:k])
        for i in range(k, len(s)):
            size = len(stack)
            if size == 0 or s[i] != stack[-1]:
                stack.append(s[i])
            elif s[i] == stack[-1]:
                if size < k:
                    stack.append(s[i])
                    if len(stack) == k and len(set(stack[-k:])) == 1:
                        stack = stack[:-k]
                else:
                    stack.append(s[i])
                    if len(set(stack[-k:])) == 1:
                        stack = stack[:-k]
        return ''.join(stack)


o=Solution()
y= o.removeDuplicates(s, k)
print(y)