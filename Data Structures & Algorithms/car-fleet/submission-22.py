class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        
        cars.sort(reverse=True)
        stack = [cars[0][1]]

        for car in cars[1:]:
            last_car = stack[-1]
            if car[1] > last_car:
                stack.append(car[1])
        
        return len(stack)


        