def arrangements(n):
    # Write your code here
    ans = 1
    visited = set([str([x for x in range(1, n+1)])])
    queue = [[x for x in range(1, n+1)]]
    while queue:
        arr = queue[0]
        del queue[0]
        tmp = arr[0]
        for i in range(1, n):
            if (tmp % (i+1) == 0 or (i+1) % tmp == 0) and (arr[i] % (i+1) == 0 or (i+1) % tmp == 0):
                new_arr = arr.copy()
                new_arr[0] = new_arr[i]
                new_arr[i] = tmp 
                if (str(new_arr) not in visited):
                    ans += 1
                    queue.append(new_arr)
                    visited.add(str(new_arr))
    return ans

print(arrangements(3))