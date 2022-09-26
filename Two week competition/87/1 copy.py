from typing import List
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        j = 0
        res = 0
        for i, t in enumerate(trainers):
            while j < len(players) and t < players[j]:
                j += 1
            if j < len(players):
                res += 1
                j += 1
            else:
                return res
        return res


