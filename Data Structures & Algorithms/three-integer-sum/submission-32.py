class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []

        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -n
            l, r = i+1, len(nums) - 1

            while l < r:
                s = nums[l] + nums[r]
                
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    result.append([n, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return result
