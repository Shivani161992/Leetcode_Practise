num = 10


class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return 'Zero'
        numbers = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        tens = {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
                80: 'Eighty', 90: 'Ninety'}
        hundreds = {1000000000: 'Billion', 1000000: 'Million', 1000: 'Thousand', 100: 'Hundred'}
        elevens = {11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                   17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

        billion = num // 1000000000
        million = (num - billion * 1000000000  )  // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000 )  // 1000
        hundred= num%1000
        englishWord = ''
        def threes(nums):
            word = ''
            if nums // 100 != 0:
                word = word + numbers[nums // 100] + ' ' +hundreds[100]

            newNum = nums % 100
            if 11 <= newNum <= 19:
                word = word + ' '+ elevens[newNum]
            else:
                if newNum // 10 != 0:
                    x= (newNum // 10) * 10
                    y= newNum % 10
                    word = word + ' '+ tens[(newNum // 10) * 10] +' ' +numbers[newNum % 10]
                else:
                    word = word + ' '+ numbers[newNum % 10]

            return word
        if billion:
            englishWord= englishWord + threes(billion) + ' Billion' + ' '
        if million:
            englishWord= englishWord + threes(million) + ' Million' + ' '
        if thousand:
            englishWord = englishWord + threes(thousand) + ' Thousand' + ' '

        englishWord = englishWord + threes(hundred)
        return englishWord



obj = Solution()
print(obj.numberToWords(num))
