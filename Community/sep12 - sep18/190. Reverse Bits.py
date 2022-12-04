class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        while n >=2:
            bits.append(n%2)
            n = n//2
        if n == 1:
            bits.append(n)
        num = 0
        print(bits)
        for i in range(len(bits)):
            num += bits[i]*2**(31-i)
        return num