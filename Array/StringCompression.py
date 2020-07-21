from typing import List
chars= ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

class Solution:
    def compress(self, chars: List[str]) -> int:
        len_nums=len(chars)
        count = 0
        prev=''
        index=0
        while index < len_nums:
            if prev != chars[index]:
                prev=chars[index]
                if prev != "" and count >1:
                    self.insert_helper(count, index)
                    count = 1
                    index = index + 1
                    len_nums = len(chars)
                else:
                    count = 1
                    index = index + 1
            elif prev == chars[index]:
                chars.pop(index)
                len_nums = len(chars)
                count= count +1

        self.insert_helper(count, index)

        return len(chars)

    def insert_helper(self, count, index):
        if count <= 9 and count > 1:
            chars.insert(index, count)
        elif count > 9:
            for i in str(count):
                chars.insert(index, i)
                index = index +1





o=Solution()
y=o.compress(chars)
print(y)
