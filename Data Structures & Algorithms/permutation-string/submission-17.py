class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        chars = [0] * 26
        curr = [0] * 26
        
        for c in s1:
            chars[ord(c) - ord('a')] += 1
        
        matches = 0

        for c in s2[:len(s1)]:
            curr[ord(c) - ord('a')] += 1
        
        for i in range(26):
            if chars[i] == curr[i]:
                matches += 1
        
        if matches == 26:
            return True
        
        for i in range(len(s1), len(s2)):
            oldC = s2[i - len(s1)]

            if chars[ord(oldC) - ord('a')] == curr[ord(oldC) - ord('a')]:
                matches -= 1

            curr[ord(oldC) - ord('a')] -= 1

            if chars[ord(oldC) - ord('a')] == curr[ord(oldC) - ord('a')]:
                matches += 1

            c = s2[i]

            if chars[ord(c) - ord('a')] == curr[ord(c) - ord('a')]:
                matches -= 1
            
            curr[ord(c) - ord('a')] += 1

            if chars[ord(c) - ord('a')] == curr[ord(c) - ord('a')]:
                matches += 1
            
            print(matches)
            
            if matches == 26:
                return True
        return False


            


