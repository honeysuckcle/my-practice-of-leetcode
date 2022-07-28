from typing import List

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

class FoodRatings:
    def compare(self, food1, food2):
        if self.food_dict[food1]['rating'] > self.food_dict[food2]['rating']:
            return True
        elif self.food_dict[food1]['rating'] == self.food_dict[food2]['rating'] and food1 < food2:
            return True
        return False

    def insert(self, arr, n):
        arr.append(n)
        i = len(arr) - 1
        while int(i/2) > 0:
            parent = int(i/2)
            if self.compare(arr[i], arr[parent]):
                swap(arr, i, parent)
            i = parent
        return arr

    def adjust(self, heap, node):
        if self.compare(heap[node*2], heap[node]):
            swap(heap, node, node*2)
        if node * 2 + 1 < len(heap) and self.compare(heap[node*2+1], heap[node]):
            swap(heap, node, node*2)

    def delete_node(self, heap, food):
        index = 0
        for i in range(1, len(heap)):
            if heap[i] == food:
                index = i
                heap.remove(food)
                break
        
        node = index
        if node*2 < len(heap) and self.compare(heap[node*2], heap[node]):
            swap(heap, node, node*2)
            self.adjust(heap, node*2)
        if node * 2 + 1 < len(heap) and self.compare(heap[node*2+1], heap[node]):
            swap(heap, node, node*2)
            self.adjust(heap, node*2+1)
        return heap


    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_dict = {}
        for i in range(len(foods)):
            self.food_dict[foods[i]] = {'rating':ratings[i], 'cuisine':cuisines[i]}

        self.suisine_dict = {}
        for i in range(len(cuisines)):
            c = self.suisine_dict.get(cuisines[i])
            if c == None:
                self.suisine_dict[cuisines[i]] = [0, foods[i]]
            else:
                self.suisine_dict[cuisines[i]] = self.insert(self.suisine_dict[cuisines[i]], foods[i])


    def changeRating(self, food: str, newRating: int) -> None:
        self.food_dict[food]['rating'] = newRating
        c = self.food_dict[food]['cuisine']
        heap = self.suisine_dict[c]
        self.suisine_dict[c] = self.delete_node(heap, food)
        self.insert(self.suisine_dict[c], food)

    def highestRated(self, cuisine: str) -> str:
        res = self.suisine_dict[cuisine]
        if res != None and len(res)>=2:
            return res[1]

foodRatings = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
foodRatings.highestRated("korean") # 返回 "kimchi"
                                    # "kimchi" 是分数最高的韩式料理，评分为 9 。
foodRatings.highestRated("japanese") # 返回 "ramen"
                                      # "ramen" 是分数最高的日式料理，评分为 14 。
foodRatings.changeRating("sushi", 16) # "sushi" 现在评分变更为 16 。
foodRatings.highestRated("japanese") # 返回 "sushi"
                                      # "sushi" 是分数最高的日式料理，评分为 16 。
foodRatings.changeRating("ramen", 16) # "ramen" 现在评分变更为 16 。
foodRatings.highestRated("japanese") # 返回 "ramen"
                                      # "sushi" 和 "ramen" 的评分都是 16 。
                                      # 但是，"ramen" 的字典序比 "sushi" 更小。