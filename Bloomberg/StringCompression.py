from typing import List
from collections import Counter
chars= ["a","a","b","b","b","b","b","b","b","b","b","b","b","b", "c"]

class Solution:
    def compress(self, chars: List[str]) -> int:
        index=0
        hold=''
        count=0
        while index < len(chars):
            if hold=="":
                hold=chars[index]
                index= index + 1
                count = count +1
            elif hold == chars[index]:
                if index + 1 < len(chars) and chars[index]== chars[index + 1]:
                    count = count +1
                    chars.pop(index)
                else:
                    break
            elif hold != chars[index]:
                if count >1 and count <=9:
                    chars.insert(index, count)
                    index = index + 1

                elif count > 9:
                    for i in str(count):
                        chars.insert(index, i)
                        index = index + 1
                hold = chars[index]
                count = 1
        return chars
obj=Solution()
print(obj.compress(chars))