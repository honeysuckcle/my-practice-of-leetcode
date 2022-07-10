class SmallestInfiniteSet:

    def __init__(self):
        self.size = 10
        self.end = 10
        self.arr = [i for i in range(1, 10)]
        self.arr.sort(reverse=True)

    def expend(self):
        self.arr = [i for i in range(self.end, self.end + self.size)]
        self.end += self.size
        self.arr.sort(reverse=True)

    def popSmallest(self) -> int:
        if len(self.arr) == 0:
            self.expend()
        return self.arr.pop()


    def addBack(self, num: int) -> None:
        if len(self.arr) == 0:
            self.expend()
        if num < self.arr[-1]:
            self.arr.append(num)
        flag = False
        if num < self.arr[0] and num > self.arr[-1]:
            for i in self.arr:
                if i == num:
                    flag = True
            if flag == False:
                self.arr.append(num)
                self.arr.sort(reverse=True)



# ["SmallestInfiniteSet","popSmallest","addBack","popSmallest","popSmallest","popSmallest","addBack","addBack","popSmallest","popSmallest"]
# [[],[],[1],[],[],[],[2],[3],[],[]]
# [null,1,null,1,2,3,null,null,2,3]
smallestInfiniteSet = SmallestInfiniteSet()
smallestInfiniteSet.popSmallest() # 返回 1 ，因为 1 是最小的整数，并将其从集合中移除。
smallestInfiniteSet.addBack(91) 

smallestInfiniteSet.popSmallest()
smallestInfiniteSet.popSmallest()
smallestInfiniteSet.popSmallest()
smallestInfiniteSet.popSmallest()                    
smallestInfiniteSet.popSmallest() 
smallestInfiniteSet.popSmallest() 
smallestInfiniteSet.popSmallest() 
smallestInfiniteSet.popSmallest() 
smallestInfiniteSet.popSmallest() 