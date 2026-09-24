class Solution:

    def encode(self, strs: List[str]) -> str:
        length = ""
        sentence = ""

        for i in range(len(strs)):
            length += str(len(strs[i]))
            sentence += strs[i]
            
            if i != len(strs) - 1:
                length += ","
            else:
                length += "#"
            
        return length + sentence

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        length = ""

        for char in s:
            if char != "#":
                length += char
                s = s[1:]
            else:
                s = s[1:]
                break
        
        length_lst = length.split(",")
        strs = []
        
        for i in length_lst:
            strs.append(s[:int(i)])
            s = s[int(i):]
        
        return strs
