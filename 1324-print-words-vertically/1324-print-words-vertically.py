class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        max_length = 0
        for word in s:
            max_length = max(max_length, len(word))
        
        vertical_words = ['' for _ in range(max_length)]
        for i in range(max_length):
            for j in range(len(s)):
                
                vertical_words[i] += s[j][i] if i<len(s[j]) else ' '
                
        for i  in range(len(vertical_words)):
            j=len(vertical_words[i])-1
            while vertical_words[i][j]==' ': j-=1
            vertical_words[i] = vertical_words[i][:j+1]
        return vertical_words
            