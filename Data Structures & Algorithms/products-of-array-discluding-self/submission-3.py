# https://neetcode.io/problems/products-of-array-discluding-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lst = nums.copy()
        # p = 1
        # lst_p = []

        # if 0 in nums:
        #     lst.remove(0)

        #     for l in lst: p *= l

        #     for n in nums:
        #         elem = p if n == 0 else 0
        #         lst_p.append(p if n == 0 else 0)
        
        # else:
        #     for l in lst: p *= l
            
        #     for n in nums:
        #         lst_p.append(p // n)
        
        # return lst_p

        lst = [1] * len(nums)

        pref = 1

        for i in range(len(nums)):
            lst[i] = pref
            pref *= nums[i]
        
        suff = 1

        for i in range(len(nums)-1, -1, -1):
            lst[i] *= suff
            suff *= nums[i]
        
        return lst
