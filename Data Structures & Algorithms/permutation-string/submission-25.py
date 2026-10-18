class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1map = [0] * 26
        s2map = [0] * 26
        
        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1map[i] == s2map[i]:
                matches += 1
        
        if matches == 26:
            return True
        
        for i in range(len(s1), len(s2)):
            rm = s2[i - len(s1)]
            if s1map[ord(rm) - ord('a')] == s2map[ord(rm) - ord('a')]:
                matches -= 1
            
            s2map[ord(rm) - ord('a')] -= 1
            if s1map[ord(rm) - ord('a')] == s2map[ord(rm) - ord('a')]:
                matches += 1
            
            add = s2[i]
            if s1map[ord(add) - ord('a')] == s2map[ord(add) - ord('a')]:
                matches -= 1

            s2map[ord(add) - ord('a')] += 1
            if s1map[ord(add) - ord('a')] == s2map[ord(add) - ord('a')]:
                matches += 1
            
            if matches == 26:
                return True
        return False

            


            
