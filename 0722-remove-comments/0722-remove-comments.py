class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        source = '#'.join(source)
        i = 0
        while i <len(source)-1:
            if source[i:i+2] =='/*':
                j = i+2
                while source[j:j+2]!='*/':j+=1
                source= source[:i] + source[j+2:]
            elif source[i:i+2] =='//':
                j = i+2
                while j<len(source) and source[j]!='#':j+=1 
                source = source[:i] + source[j:]
            else: i+=1
       
        source =source.split('#')
        source = [i for i in source if len(i)>=1]
        
        return source