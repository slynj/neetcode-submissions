# https://neetcode.io/problems/is-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        s = s.lower()

        while(l < r):
            if (s[l].isalnum() and s[r].isalnum()): 
                if s[l] != s[r]: return False
                else:
                    l += 1
                    r -= 1
            
            if not s[l].isalnum(): l += 1
            if not s[r].isalnum(): r -= 1

        return True

        # s = s.lower()

        # for c in s:
        #     if not (c.isalnum()): s = s.replace(c,'')

        # index = len(s) - 1

        # for i in range(0, len(s)//2):
        #     if s[i] != s[index-i]: 
        #         return False
        # return True