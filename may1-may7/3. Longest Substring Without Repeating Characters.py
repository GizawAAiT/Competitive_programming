class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) in [0,1]:
            return len(s)
        cur_substring= set()
        a=0
        b=1
        Ans = 0
        cur_substring.add(str(s[0]))
        # print cur_substring
        while  b<len(s) :
            if  s[b] not in cur_substring:
                cur_substring.add(str(s[b]))
                b +=1
            else:
                Ans = max(Ans, b-a)
                while s[b]  in cur_substring:
                    cur_substring.remove(str(s[a]))
                    a+=1
        Ans = max(Ans, b-a)
        return Ans