from typing import List
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0 for i in range(n)]
        last_state = 'end'
        last_time = -1
        last_task = 0
        stack = []
        for log in logs:
            task, state, time = log.split(':')
            task = int(task)
            time = int(time)
            
            if state == 'start':
                stack.append(task)
                if last_state == 'end':
                    res[stack[-1]] += time - last_time - 1
                    last_state = 'start'
                    last_time = time
                    last_task = task
                elif last_state == 'start':
                    res[last_task] += time - last_time
                    last_time = time
                    last_task = task
            elif state == 'end':
                stack.pop()
                if last_state == 'start' and last_task == task:
                    res[task] += time - last_time + 1
                else:
                    res[task] += time - last_time
                last_state = 'end'
                last_time = time
                last_task = task
        return res


print(Solution().exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]))