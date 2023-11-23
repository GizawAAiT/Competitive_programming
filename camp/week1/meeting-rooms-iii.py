# from heapq import *
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_rooms, reserved = [room for room in range(n)], []
        heapify(free_rooms)

        host = defaultdict(int)
        for start, end in meetings:
            while reserved and reserved[0][0] <= start:
                heappush(free_rooms, heappop(reserved)[1])
            
            if free_rooms:
                room = heappop(free_rooms)

            else:
                free_time, room = heappop(reserved)
                delay = free_time - start
                end += delay

            heappush(reserved, (end, room))
            host[room] += 1

        maxHostRoom = 0
        for room in range(1, n):
            if host[room] > host[maxHostRoom]:
                maxHostRoom = room  

        return maxHostRoom









