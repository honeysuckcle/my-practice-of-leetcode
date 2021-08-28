"""
Date: 2021/7/25
hash table
找到只出现一次的数字，作为head，一个一个往下找
python字典
超时，但尚不明原因
"""

def restoreArray(adjacentPairs):
    hashMap = {}
    for pair in adjacentPairs:
        item = hashMap.get(pair[0])
        if item != None:
            hashMap[pair[0]] = item + [pair[1]]
        else:
            hashMap[pair[0]] = [pair[1]]

        item = hashMap.get(pair[1])
        if item != None:
            hashMap[pair[1]] = item + [pair[0]]
        else:
            hashMap[pair[1]] = [pair[0]]

    head = 0
    for key in hashMap:
        if len(hashMap[key]) == 1:
            head = key
            break
    
    key = head
    res = [head]
    while len(hashMap[key]) != 0:
        right = hashMap[key].pop() 
        if right in res:
            if len(hashMap[key]) == 0:
                return res
            else:
                key = hashMap[key].pop()
                res.append(key)
        else:
            key = right
            res.append(key)
        
    return res

print (restoreArray([[2,1],[3,4],[3,2]]))

print(restoreArray([[4,-2],[1,4],[-3,1]]))
