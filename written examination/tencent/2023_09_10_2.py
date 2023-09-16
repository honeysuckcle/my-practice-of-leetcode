import numpy as np
def norm(x):
    return (x-np.min(x))/(np.max(x)-np.min(x))
n = int(input())
matrix = []
for i in range(n):
    line = list(map(float, input().split()))
    matrix.append(line)
    
v0 = list(map(float, input().split()))
v0 = np.array(v0)

matrix = np.array(matrix)

v1 = np.dot(matrix, v0.T)
pre = v1[0] / v0[0]
v0 = v1
v1 = np.dot(matrix, v0.T)
cur = v1[0]/v0[0]
while abs(cur - pre) > 1e-5:
    pre = cur
    v0 = v1
    v1 = np.dot(matrix, v0.T)
    v1 = (v1-np.mean(v1)) / np.std(v1)
    
    cur = v1[0] / v0[0]
print(round(cur, 2))