class Solution:
    def compress(self, chars: List[str]) -> int:
        writePos = 0
        seek = 0

        while seek < len(chars):
            char = chars[seek]
            count = 0

            while seek < len(chars) and chars[seek] == char:
                count += 1
                seek += 1
            
            chars[writePos] = char
            writePos += 1

            if count > 1:
                for c in str(count):
                    chars[writePos] = c
                    writePos += 1
        return writePos
