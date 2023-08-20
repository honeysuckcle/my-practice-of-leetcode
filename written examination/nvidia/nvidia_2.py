def maxEvents(arrival, duration):
    # Write your code here
    pairs = list(zip(arrival, duration))
    pairs.sort(key=lambda x:x[0]+x[1])
    dp = [0] * (max(arrival)+max(duration)+1)
    n = len(arrival)
    for i in range(n):
        dp[pairs[i][0]+pairs[i][1]] = max(dp[pairs[i][0]+pairs[i][1]], max(dp[:pairs[i][0]+1])+1)
    return max(dp)

# print(maxEvents([978, 409, 229, 934 ,299, 982, 636, 14, 866, 815, 64, 537, 426, 670, 116, 95, 630],
#                 [502, 518, 196, 106, 405, 452, 299, 189, 124, 506, 883, 753, 567, 717, 338, 439, 145]))
print(maxEvents([1,3,5], [2,2,2]))