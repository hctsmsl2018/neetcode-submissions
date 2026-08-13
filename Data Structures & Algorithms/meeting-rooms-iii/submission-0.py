from heapq import heapify, heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        uses_counts = [0] * n
        open_rooms = list(range(n))
        heapify(open_rooms)
        room_queue = []

        for start, end in meetings:
            while len(room_queue) > 0 and room_queue[0][0] <= start:
                _, room = heappop(room_queue)
                heappush(open_rooms, room)

            if len(room_queue) == n:
                end_time, room = heappop(room_queue)

                uses_counts[room] += 1
                heappush(room_queue, (end_time + end - start, room))
            else:
                next_room = heappop(open_rooms)
                uses_counts[next_room] += 1
                heappush(room_queue, (end, next_room))

        return max(range(n), key=lambda x: uses_counts[x])