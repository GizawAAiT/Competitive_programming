class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(' ')
        for w in sentence:
            if len(w) >= len(searchWord) and w[:len(searchWord)]== searchWord:
                return sentence.index(w)+1
        return -1 