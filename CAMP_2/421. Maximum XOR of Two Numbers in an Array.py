# 421. Maximum XOR of Two Numbers in an Array
# class TrieNode:
#     def __init__(self):
#         self.children = {}

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        cur = root = {}
        n = nums[0]
        for i in range(31, -1, -1):
            bit = 1 if (1<<i & n)>0 else 0
            cur[bit] = {}
            cur = cur[bit]
        
        answer = 0
        for n in nums:
            temp = root
            ans = 0
            for i in range(31, -1, -1):
                bit = 1 if (1<<i & n)>0 else 0    
                if (bit+1)%2 in temp:
                    ans += 1<<i
                    temp = temp[(bit+1)%2]
                else:
                    temp = temp[bit]
            answer = max(ans, answer)    

            cur = root
            for i in range(31, -1, -1):
                bit = 1 if (1<<i & n)>0 else 0
                if bit not in cur:
                    cur[bit] = {}
                cur = cur[bit]
            
        return answer