class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.insert(0,0)
        sentence = ''
        for i in range(1,len(spaces)):
            sentence += (s[spaces[i-1]:spaces[i]] + ' ')
        sentence += s[spaces[-1]:]
        return sentence
    