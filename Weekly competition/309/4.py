from cmath import inf
class Solution:
    def mostBooked(self, n: int, meetings) -> int:
        end_time = [0 for _ in range(n)]
        meeting = [0 for _ in range(n)]
        for s, e in sorted(meetings, key=lambda p :p[0]):
            empty_room = -1
            for i in range(n):
                if end_time[i] <= s:
                    empty_room = i
                    break
            room = 0
            if empty_room == -1:
                time = +inf
                for i in range(n):
                    if end_time[i] < time:
                        room = i
                        time = end_time[i]
                empty_room = room
            meeting[empty_room] += 1
            if end_time[empty_room] <= s:
                end_time[empty_room] = e
            else:
                end_time[empty_room] += e-s
        max_m = 0
        max_r = 0
        for i in range(n):
            if max_m < meeting[i]:
                max_m = meeting[i]
                max_r = i
        return max_r

s = Solution()
print(s.mostBooked(100,