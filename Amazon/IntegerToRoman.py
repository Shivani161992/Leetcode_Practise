num=3
class Solution:
    def intToRoman(self, num: int) -> str:
        roman= { 1000 : 'M',
                 900: 'CM',
                 500 : 'D',
                 100: 'C',
                 90: 'XC',
                 50: 'L', 10: 'X', 5: 'V', 4:'IV', 1:"I"
        }
        romanWord=''
        for r in roman:
            romanWord= romanWord +  (num // r) * roman[r]
            num = num % r
        return romanWord

obj=Solution()
print(obj.intToRoman(num))