class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                chars[idx] += 1
            
            groups[tuple(chars)].append(s)

        return list(groups.values())