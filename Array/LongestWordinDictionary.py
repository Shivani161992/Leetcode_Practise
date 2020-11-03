from typing import List
words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
class Solution:
    def longestWord(self, words: List[str]) -> str:
        if len(words) != 0:
            words.sort()

            longest_word=words[0]
            hold=words[0]
            for i in range(1, len(words)):
                if hold in words[i]:
                    longest_word= words[i] if len(words[i]) >= len(longest_word) else longest_word

                    hold=words[i]
                elif hold not in words[i]:
                    hold = words[i]
            return longest_word



obj=Solution()
print(obj.longestWord(words))