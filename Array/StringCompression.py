from typing import List
chars= ["a","a","b","b","c","c","c"]

class Solution:
    def compress(self, chars: List[str]) -> int:
        element = []
        count = 0
        for i in chars:
            hold= chars.count(i) # count number of elements
            if i not in element:
                element.append(i)
                count = count + 1
                if hold != 1:
                    for j in str(hold):
                        count = count + 1
        return count



o=Solution()
y=o.compress(chars)
print(y)
