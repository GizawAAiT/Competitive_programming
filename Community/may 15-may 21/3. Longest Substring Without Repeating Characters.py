class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        chrset=set()
        
        result = 0
        
        p1=p2=0
        while p2<len(s):
            if s[p2] in chrset:
                chrset.remove(s[p1])
                p1+=1
                print('p1',p1)
                
            else:                
                chrset.add(s[p2])
                p2+=1
                print('p2',p2)
                result = max(result,p2-p1)
        return result
                