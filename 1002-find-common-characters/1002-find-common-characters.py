class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def frq(word):
            res = [0]*26
            for c in word:
                res[ord(c)-ord('a')] +=1
            return res
        
        for i in range(len(words)):
            words[i] = frq(words[i])
        answer = []
        for i in range(26):
            minimum = float('inf')
            for j in range(len(words)):
                minimum = min(minimum, words[j][i])
            answer.extend([chr(i+ord('a'))]*minimum)
        return answer
            
            
            
            
        

            