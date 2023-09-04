class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        dic = {}
        for i in range(ord('z')-ord('a')+1):
            dic[i] = chr(ord('a')+i)
        print(dic)
        pref = [0 for _ in range(len(s)+1)]
        for shift in shifts:
            pref[shift[0]] += 1 if shift[2] ==1 else -1
            pref[shift[1]+1] -= 1 if shift[2] ==1 else -1
        
        for i in range(1,len(pref)):
            pref[i] += pref[i-1]
        
        res = ''
        print(pref,s)
        for i in range(len(s)):
            print((ord(s[i]) - ord('a'))) 
            res +=  dic[((ord(s[i]) - ord('a')) + pref[i] + ((abs(pref[i])//26)+1)*26  )  %  26]
            # print(dic[((ord(s[i]) - ord('a')) + pref[i] + 26)//26])
        return res