class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a),len(b))
        if len(a) < length:
            a = "0"*(length-len(a)) + a
        if len(b) < length:
            b = "0"*(length-len(b)) + b
        
        rem = 0
        i = 1
        res = ""
        while i <= length:
            v = rem + int(a[-i]) + int(b[-i]) 
            if v < 2:
                res = str(v) + res
                rem = 0
            else:
                rem = 1
                res = str(v-2) + res
                
            i +=1
        if rem:
            res = "1" + res
        return res