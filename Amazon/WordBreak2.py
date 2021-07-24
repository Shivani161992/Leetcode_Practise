from typing import List

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        x=[1,2,3]
        y=[4, 5, 6]
        z= zip(x, y)
        allWordBreaks = []
        wordDictSet = set(wordDict)
        word = s
        hold = ""
        self.findWordBreak(word, wordDictSet, allWordBreaks, hold)
        return allWordBreaks

    def findWordBreak(self, word, wordDictSet, allWordBreaks, hold):
        if word == "":
            newHold= hold.strip()
            allWordBreaks.append(newHold)
        else:
            i = 0
            for j in range(1, len(word)+1):
                z=word[i:j]
                if word[i:j] in wordDictSet:
                    x= word[j:]
                    y= hold + word[i:j] + ' '
                    self.findWordBreak(word[j:], wordDictSet, allWordBreaks, hold + word[i:j] + ' ')
            return



obj = Solution()
print(obj.wordBreak(s, wordDict))
