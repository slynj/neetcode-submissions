class Solution:
    def compress(self, chars: List[str]) -> int:
        check = 0
        writePos = 0

        while check < len(chars):
            char = chars[check]
            count = 0
            
            while check < len(chars) and chars[check] == char:
                check += 1
                count += 1
            
            chars[writePos] = char
            writePos += 1

            if count > 1:
                for c in str(count):
                    chars[writePos] = c
                    writePos += 1
        
        return writePos



            