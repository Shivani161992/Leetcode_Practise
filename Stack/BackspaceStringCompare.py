S = "ab#c"
T = "ad#c"
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        x = self.helper(S)
        y = self.helper(T)
        return True if x == y else False

    def helper(self, Z):
        hold = []
        for i in Z:
            if i != '#':
                hold.append(i)
            elif i == '#' and len(hold) !=0:
                hold.pop()

        return ''.join(hold)
o=Solution()
y=o.backspaceCompare(S, T)
print(y)