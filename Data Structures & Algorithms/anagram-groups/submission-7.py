class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            string = "".join(sorted(s))
            groups[string].append(s)
        
        return list(groups.values())