class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        def rev(w):
            w = list(w)
            i = 0
            while i < len(w)//2:
                w[i], w[-1-i] = w[-1-i], w[i] 
                i+=1
            return "".join(w)
        words = s.split()
        print(words)
        for i in range(len(words)):
            words[i] = rev(words[i])
        return " ".join(words) 