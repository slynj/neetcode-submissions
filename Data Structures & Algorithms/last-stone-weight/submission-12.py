class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 2:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)

            newStone = max1 - max2

            if newStone != 0:
                heapq.heappush(stones, newStone)
        
        if len(stones) == 1:
            return abs(stones[0])
        else:
            return abs(stones[0] - stones[1])


        