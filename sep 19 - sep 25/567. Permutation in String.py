class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d = {}
        colec1,colec2 = [0]*26, [0]*26
        
        for i in range(len(s1)):
            colec1[ord(s1[i])-ord("a")] +=1
            colec2[ord(s2[i])-ord("a")] +=1
        i, j = 0, len(s1)
        print(f"""original\n{colec1}\n{colec2}""")
        while j< len(s2): 
            if colec1 == colec2:
                return True
            
            colec2[ord(s2[i])-ord("a")] -=1
            colec2[ord(s2[j])-ord("a")] +=1 
            j+=1
            i+=1
            print(f"""\n{colec1}\n{colec2}""")
        if colec1 == colec2:
            return True
        return False