from typing import List
import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        clear_paragraph = re.sub(r'[^\w\s]', '', paragraph.lower())
        word_freq= Counter(clear_paragraph.split(sep=' ')).most_common()
        word_byfreq= [word[0] for word in word_freq if word[0] not in banned]
        if len(word_byfreq)!=0:
            return word_byfreq[0]
        return ''

obj=Solution()
print(obj.mostCommonWord(paragraph, banned))