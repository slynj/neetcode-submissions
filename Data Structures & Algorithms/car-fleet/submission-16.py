class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        
        cars.sort(reverse=True)
        fleets = [cars[0][1]]

        for car in cars[1:]:
            last_car = fleets[-1]
            if car[1] > last_car:
                fleets.append(car[1])
        print(fleets)
        return len(fleets)


        