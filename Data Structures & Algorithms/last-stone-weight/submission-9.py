class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 2:
            heapq.heapify_max(stones)

            maxStone = stones[0]
            maxStone2 = max(stones[1], stones[2])

            newStone = maxStone - maxStone2

            stones.append(min(stones[1], stones[2]))
            stones = stones[3:]

            if newStone > 0:
                stones.append(newStone) 
        
        match (len(stones)):
            case 1:
                return stones[0]
            case 2: 
                return abs(stones[1] - stones[0])
        
        