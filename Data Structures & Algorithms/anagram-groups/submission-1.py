# https://neetcode.io/problems/anagram-groups

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # lst_h = {}

        # for s in strs:
        #     a = ''.join(sorted(s))

        #     if a not in lst_h:
        #         lst_h[a] = []

        #     lst_h[a].append(s)

        # return list(lst_h.values())

        
        list_h = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                i = ord(c) - ord('a')
                count[i] += 1
            
            list_h[tuple(count)].append(s)
        
        return list(list_h.values())





        