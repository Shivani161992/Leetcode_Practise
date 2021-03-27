from typing import List

digits = "23"


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
                }
        output = []
        if len(digits) != 0:
            self.combination(digits, output, keys, '')
        return output

    def combination(self, digits, output, keys, s):
        if len(digits) == 0:
            output.append(s)
        else:
            k = digits[0]
            val = keys[k]
            for v in val:

                self.combination(digits[1:], output, keys, s+v)



obj = Solution()
print(obj.letterCombinations(digits))
