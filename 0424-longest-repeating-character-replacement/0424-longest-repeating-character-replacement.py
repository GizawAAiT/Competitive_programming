class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        left = 0
        dic = defaultdict(int)
        
        result = 0
        for right in range(len(s)):
            dic[s[right]] += 1
            max_freq = max(dic.values()) 
            
            while right-left + 1 - max_freq > k:
                dic[s[left]] -= 1
                left +=1
                max_freq = max(dic.values()) 
            result = max(result, right-left+1) 
            
        return result 