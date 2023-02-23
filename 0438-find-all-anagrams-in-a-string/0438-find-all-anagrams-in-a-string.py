
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p): return []
        dic_p = Counter(p)
        def compare(dic_s)->bool:
            for key in dic_p:
                if dic_p[key]!=dic_s[key]:
                    return False
            return True
        
        result = []
        
        
        dic_s = defaultdict(int)
        
        left = 0
        for right in range(len(s)):
            dic_s[s[right]]+=1
            if right -left +1>len(p):
                dic_s[s[left]] -= 1
                left+=1            
            if right -left +1 == len(p):
                print((left,right))
                if compare(dic_s): 
                    result.append(left)
                    print(dic_s, dic_p)
            
        
        return result
#         start = 0
#         dic = defaultdict(int)
#         for end in range(window):
#             dic[s[end]]+=1
#         if compare(dic): count.append(0)
            
#         for i in range(window , len(s)):
#             # # print('entered',dic)
#             dic[s[start]]-=1
#             dic[s[i]]+=1
#             # print(dic,window)
#             if compare(dic): count.append(start+1)
#             start+=1
#         return count