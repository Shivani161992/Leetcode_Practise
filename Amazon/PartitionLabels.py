from typing import List
from collections import OrderedDict

S = "ababcbacadefegdehijhklij"


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if len(S) == 0:
            return []
        else:
            labels = []
            stchars = OrderedDict()
            for idx, s in enumerate(S):
                stchars.setdefault(s, []).append(idx)

            start = ''
            end = ''
            for k in stchars:
                indices = stchars[k]
                if start == '' and end == '':
                    start = indices[0]
                    end = indices[-1]
                if indices[-1] > end and indices[0] < end:
                    end = indices[-1]
                elif indices[-1] > end and indices[0] > end:
                    labels.append(end - start + 1)
                    start = indices[0]
                    end = indices[-1]
            labels.append(end - start + 1)
            return labels


obj = Solution()
print(obj.partitionLabels(S))
