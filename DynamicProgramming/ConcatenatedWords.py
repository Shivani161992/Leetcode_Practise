from typing import List

words = ["cat","dog","catdog"]

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordsSet = set(words)
        concatenatedWords = []
        for word in words:
            hold = []
            self.concatenate(word, wordsSet, hold, concatenatedWords)
        return concatenatedWords

    def concatenate(self, word, wordsSet, hold, concatenatedWords):
        found = False
        if word == "":
            if len(hold) > 1:
                concatenate = ''.join(hold)
                concatenatedWords.append(concatenate)
                return True
        else:
            for i in range(0, len(word)):
                newWord = word[:i + 1]
                if newWord in wordsSet:
                    hold.append(newWord)
                    found = self.concatenate(word[i + 1:], wordsSet, hold, concatenatedWords)
                    hold.pop()
                    if found == True:
                        return found

            return found

    def findAllConcatenatedWordsInADict1(self, words: List[str]) -> List[str]:
        wordsSet = set(words)
        concatenateWords = []
        for word in wordsSet:
            dp = [False] * (len(word) + 1)
            dp[0] = True
            count = 0
            for i in range(1, len(word) + 1):
                for j in range(0, i):
                    x = dp[j]
                    y = word[j:i]
                    if dp[j] == True and word[j:i] in wordsSet:
                        if word[j:i] != word:
                            count = count + 1
                        dp[i] = True
                        break
            if dp[len(word)] == True and count >= 1:
                concatenateWords.append(word)

        return concatenateWords


obj = Solution()
print(obj.findAllConcatenatedWordsInADict1(words))
