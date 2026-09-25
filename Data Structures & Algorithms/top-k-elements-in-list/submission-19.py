class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap = collections.defaultdict(int)
        count = collections.defaultdict(int)
        freqMap = collections.defaultdict(list)

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            freqMap[c].append(n)
        
        result = []

        for c in range(len(nums), 0, -1):

            for n in freqMap[c]:
                if k > 0:
                    result.append(n)
                else:
                    return result
                k -= 1
        return result




