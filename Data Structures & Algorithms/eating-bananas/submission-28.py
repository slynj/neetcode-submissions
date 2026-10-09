class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        minSpeed = r

        while l <= r:
            m = (l + r)//2
            hours = 0
            # print("m", m)

            for p in piles:
                hours += math.ceil(float(p) / m)
            
            if hours <= h:
                minSpeed = m
                r = m - 1
            else:
                l = m + 1
        
        return minSpeed
            
            
        