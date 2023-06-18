# from collections import  Counter
# t = int(input())
# for _ in range(t):
#     n, c = (int(_) for _ in input().split())
#     a = [int(_) for _ in input().split()]
#     count = Counter(a)
#     total = 0
#     for key in count.keys():
#         total += min(count[key], c)
#     print(total)
def minUploadTime(n: int, c: int, nums: List[int]) -> int:
    from collections import defaultdict
    cluster_counts = defaultdict(int)
   
    for computer in nums:
        cluster_counts[computer] += 1

    total_time = 0
    for cluster, computer_count in cluster_counts.items():
        total_time += min(c, computer_count)

    return total_time


# ```
# Example Usage:

# ```python
n, c = 10, 3
nums = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4]
minimum_time = minUploadTime(n, c, nums)
print(minimum_time) # Output: 4. 
