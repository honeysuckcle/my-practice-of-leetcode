class NumberContainers:

    def __init__(self):
        self.dict_ = {}
        self.dict_arr = {}

    def insert(self, arr, n):
        arr.append(n)
        i = len(arr) - 1
        while int(i/2) > 0:
            parent = int(i/2)
            if arr[i] < arr[parent]:
                temp = arr[i]
                arr[i] = arr[parent]
                arr[parent] = temp
            i = parent
        return arr
            
    def change(self, index: int, number: int) -> None:
        num = self.dict_arr.get(index)
        if num != None:
            # 不能直接revome，可能会破坏最小堆的结构
            self.dict_[num].remove(index)
        self.dict_arr[index] = number
        res = self.dict_.get(number)
        if res == None:
            self.dict_[number] = [0, index]
        else:
            self.dict_[number] = self.insert(self.dict_[number], index)


    def find(self, number: int) -> int:
        res = self.dict_.get(number)
        if res == None or len(res) <= 1:
            return -1
        else:
            return res[1]

obj = NumberContainers()
obj.change(1,10)
obj.change(2,10)
obj.change(3,10)
obj.change(5,10)
param_2 = obj.find(10)
obj.change(1,20)
param_2 = obj.find(10)
param_2 = obj.find(20)
param_2 = obj.find(30)