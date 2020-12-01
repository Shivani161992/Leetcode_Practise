digits='23'
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_combo = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']
                       }
        output=[]
        combo=''
        if len(digits) != 0:
            self.get_combos(digits, output, letter_combo, combo)
        return output


    def get_combos(self, digits, output, letter_combo, combo):
        if len(digits)==0:
            output.append(combo)
            return
        elif len(digits) !=0:
            for l in letter_combo[digits[0]]:
                self.get_combos(digits[1:], output, letter_combo, combo + l)


obj=Solution()
print(obj.letterCombinations(digits))