class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minSpeed = r
# 2 3 4 5 6
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            
            if hours <= h:
                minSpeed = m
                r = m - 1
            else:
                l = m + 1
        return minSpeed

