num = 58
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                 5: 'V', 4: 'IV', 1: "I"}
        convert = ''

        for r in roman:
            convert = convert + (num // r) * roman[r]
            num = num % r
        return convert

