from typing import List
from string import ascii_letters
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        worddict=set()
        for word in wordList:
            worddict.add(word)

        if endWord not in worddict:
            return 0
        else:

            queue=[beginWord]
            wordLe=len(beginWord)
            count=0
            letter='abcdefghijklmnopqrstuvwxyz'
            while len(queue) !=0:
                getSize=len(queue)
                count= count+1
                for p in range(getSize):
                    getWord=queue.pop(0)

                    for i in range(wordLe):
                        for c in letter:
                            holdWord=getWord
                            holdWord= holdWord[:i]+c+holdWord[i+1:]
                            if holdWord==endWord:
                                return count+1
                            if holdWord in worddict :
                                queue.append(holdWord)
                                worddict.remove(holdWord)
















obj=Solution()
print(obj.ladderLength(beginWord, endWord, wordList))
