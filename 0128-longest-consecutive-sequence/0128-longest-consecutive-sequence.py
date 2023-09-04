class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_sequence = 0
        
        for n in nums:
            if n-1 not in nums:
                cur_num = n
                cur_seq = 1
                while cur_num+1 in nums:
                    cur_num +=1
                    cur_seq += 1
                longest_sequence = max(longest_sequence, cur_seq)
        return longest_sequence
                