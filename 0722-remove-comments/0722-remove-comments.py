class Solution:
    def removeComments(self, s: List[str]) -> List[str]:
        s = '#'.join(s)
        print(s)
        i = 0
        while i <len(s)-1:
            if s[i:i+2] =='/*':
                j = i+2
                while s[j:j+2]!='*/':j+=1
                s = s[:i] + s[j+2:]
            elif s[i:i+2] =='//':
                j = i+2
                while j<len(s) and s[j]!='#':j+=1 
                s = s[:i] + s[j:]
            else: i+=1
       
        s =s.split('#')
        s = [i for i in s if len(i)>=1]
        
        return s