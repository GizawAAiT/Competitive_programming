class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        
        indx = 0
        while indx < len(words):
            cur = []
            length = 0
            while indx < len(words) and length + len(words[indx]) <= maxWidth:
                cur.append(words[indx])
                length += len(words[indx]) + 1
                indx += 1
                
            if indx >= len(words) or len(cur) < 2:
                result.append(" ".join(cur) + " "*(maxWidth-length+1))
                
            else:
                extra = maxWidth - (length -1)
                rem, quo = extra %(len(cur)-1), extra //(len(cur)-1) 
                
                s = cur[0]
                for i in range(1, len(cur)):
                    if i <= rem:
                        s += " "*(quo + 2)
                    else:
                        s += " "*(quo + 1)
                    s += cur[i]
                result.append(s)
        return result 
                