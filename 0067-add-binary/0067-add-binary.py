class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1, n2, carry = int(a, 2), int(b, 2), 0
        
        result = []
        while n1 or n2 or carry:
            a, b = n1 & 1, n2 & 1
            result.append(str(a ^ b ^ carry))
            carry = (a & b) | (a & carry) | (b & carry)
            
            n1 >>= 1
            n2 >>= 1
        # if not result: result.append('0')    
        return ''.join(reversed(result)) if result else '0'