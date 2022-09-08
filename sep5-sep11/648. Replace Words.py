class Solution:
    def replaceWords(self, dic: List[str], sentence: str) -> str:
        dic = set(dic)
        
        words = sentence.split(" ")
        
        for wd in range(len(words)):
            i = 0
            while i<len(words[wd]):
                if words[wd][:i+1] in dic:
                    words[wd] = words[wd][:i+1]
                    break
                i+=1
        return " ".join(words)
