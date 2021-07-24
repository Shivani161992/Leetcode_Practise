from typing import List
from collections import defaultdict, deque
from string import ascii_lowercase
beginWord = "red"
endWord = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordListSet= set(wordList)
        if endWord not in wordListSet:
            return []
        else:
            if beginWord in wordListSet:
                wordListSet.remove(beginWord)
            allLadders=[]
            levels={}
            adjList= defaultdict(list)
            self.createAdjList(beginWord, endWord, wordListSet, levels, adjList, allLadders)
            return allLadders

    def createAdjList(self, beginWord, endWord, wordListSet, levels, adjList, allLadders):
        bfsQueue=deque()
        bfsQueue.append(beginWord)
        count= 1
        endWordFound=False
        levels[beginWord]=1
        while bfsQueue:
            queueSize= len(bfsQueue)
            count = count + 1
            if endWordFound== False:
                for q in range(0, queueSize):
                    getNode=bfsQueue.popleft()
                    for i in range(0, len(getNode)):
                        for l in ascii_lowercase:
                            newWord=getNode[:i] + l + getNode[i+1:]
                            if newWord!= endWord:
                                if newWord in wordListSet and newWord not in levels:
                                    levels[newWord] = count
                                    bfsQueue.append(newWord)
                                    adjList[getNode].append(newWord)
                                elif newWord in wordListSet and newWord in levels:
                                    getLevel= levels[newWord]
                                    if getLevel==count:
                                        adjList[getNode].append(newWord)
                            elif newWord == endWord:
                                levels[newWord] = count
                                endWordFound = True
                                adjList[getNode].append(newWord)
            else:
                break
        ladder=[]

        self.dfs(beginWord, endWord, adjList, allLadders, ladder)
        print(levels, adjList)


    def dfs(self, beginWord, endWord, adjList, allLadders, ladder):
        ladder.append(beginWord)
        if beginWord in adjList:
            getChildren= adjList[beginWord]
            for child in getChildren:
                self.dfs(child, endWord,  adjList, allLadders, ladder)
                ladder.pop()
            return
        else:
            if beginWord== endWord:
                allLadders.append(ladder.copy())
            return










obj=Solution()
print(obj.findLadders(beginWord, endWord, wordList))
