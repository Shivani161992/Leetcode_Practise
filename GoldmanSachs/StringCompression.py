from typing import List
chars= ["a","a","b","b","b","b","b","b","b","b","b","b","b","b", 'c']
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1 or len(chars) == 0:
            return len(chars)
        else:
            idx = 0
            #create move pointer which will be moving
            midx = 0
            #hold character
            hold = ''
            #count
            count = 0
            while idx < len(chars):
                if hold == '':
                    hold= chars[idx]
                    count =  count + 1
                    midx = midx + 1
                elif hold != '':
                    if len(chars) == midx:
                        break
                    if hold == chars[midx]:
                        count = count + 1
                        chars.pop(midx)
                    elif hold != chars[midx]:
                        if count == 1:
                            idx= midx
                            midx = idx
                        elif count > 1 and count <= 9:
                            chars.insert(midx, str(count))
                            idx = midx + 1
                            midx = idx
                        elif count > 9:
                            for c in str(count):
                                chars.insert(midx, c)
                                idx = midx + 1
                                midx = idx
                        count = 0
                        hold = ''
            if count > 1 and count <= 9:
                chars.append(str(count))
            elif count > 9:
                for c in str(count):
                    chars.append(str(c))

            return len(chars)


o=Solution()
y=o.compress(chars)
print(y)

