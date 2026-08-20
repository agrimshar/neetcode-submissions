class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            arr.append((position[i], time))

        arr.sort(reverse=True)

        fleets = 0
        max_time = 0

        for _, time in arr:
            if time > max_time:
                fleets += 1
                max_time = time

        return fleets
