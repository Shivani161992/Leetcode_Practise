s="abc"
#s="aba"
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if (s==s[::-1] or s==""):
            return True
        else:
            i=0
            j=len(s)-1
            while i != j:
                if(s[i] == s[j]):
                    i = i + 1
                    j = j - 1
                elif(s[i] != s[j]):
                    x= s[:i] + s[(i+1):]
                    x_x = x[::-1]
                    y=s[:j] + s[(j+1):]
                    y_y = y[::-1]
                    if (x == x_x):
                        return True
                    elif (y == y_y):
                        return True
                    else:
                        return False




o=Solution()
y=o.validPalindrome(s)
print(y)