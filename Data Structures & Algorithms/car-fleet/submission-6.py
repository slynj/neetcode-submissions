class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            t = (target - position[i]) / speed[i]
            cars.append((position[i], t))
        
        cars.sort(reverse=True)

        stack = [cars[0]]

        for c in cars[1:]:
            time = stack[-1][1]
            if c[1] > time:
                stack.append(c)

        return len(stack)

