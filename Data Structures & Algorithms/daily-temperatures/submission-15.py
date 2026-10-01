class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [(temp, idx), ...]
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
                continue

            while stack and stack[-1][0] < temperatures[i]:
                (temp, idx) = stack.pop()
                result[idx] = i - idx

            stack.append((temperatures[i], i))
        
        return result

            





        