class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []

        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [nums]
            else:
                return []

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-1):
                sum_2 = nums[i] + nums[j]

                if -1 * sum_2 in nums[j+1:]:
                    tsum = [nums[i], nums[j], -1 * sum_2]
                    print("hi", tsum)
                    tsum.sort()
                    lst.append(tsum)
                    # lst.append([])
        print("lr", lst)
        
        tuple_lst = set(tuple(n) for n in lst)
        print("pr", tuple_lst)
        lst_tuple = [list(n) for n in tuple_lst]
        return lst_tuple

        