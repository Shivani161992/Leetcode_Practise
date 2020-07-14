n=5
class Solution:
    def factorial(self, n):
        product=1
        while n !=0:
            product = product * n
            n= n - 1

        return product
o=Solution()
y=o.factorial(n)
print(y)