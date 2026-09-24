class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        
        l, r = 0, len(heights) - 1
        maxAmount = 0

        while l < r:
            if heights[l] < heights[r]:
                maxAmount = max(maxAmount, (r - l) * heights[l])
                l += 1
            else:
                maxAmount = max(maxAmount, (r - l) * heights[r])
                r -= 1
        return maxAmount