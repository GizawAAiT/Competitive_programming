
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p): return []
        count = []
        window = len(p)
        p = Counter(p)
        
        def compare(dic)->bool:
            for key in p:
                if p[key]!=dic[key]:
                    return False
            return True
        
        start = 0
        dic = defaultdict(int)
        for end in range(window):
            dic[s[end]]+=1
        if compare(dic): count.append(0)
            
        for i in range(window , len(s)):
            # # print('entered',dic)
            dic[s[start]]-=1
            dic[s[i]]+=1
            # print(dic,window)
            if compare(dic): count.append(start+1)
            start+=1
        return count