from collections import defaultdict
from math import log
T = int(input())
for _ in range(T):
    D, W, t = list(map(float, input().split()))
    artical_arr = []
    tf = defaultdict(float)
    idf = defaultdict(set)
    for i in range(int(D)):
        artical_arr.append(input().split())
        for j, word in enumerate(artical_arr[i]):
            tf[word] += 1
            idf[word].add(i)
    max_ans = 0
    for k in tf.keys():
        tfidf = tf[k]/(W*D) * log(D/(len(idf[k])+1))
        if tfidf > max_ans:
            max_ans = tfidf
    if max_ans > t:
        print(1)
    else:
        print(0)