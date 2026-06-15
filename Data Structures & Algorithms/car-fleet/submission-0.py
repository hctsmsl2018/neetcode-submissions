class Solution:
    def check_will_intersect(self, pos_1, speed_1, pos_2, speed_2):
        if speed_1 == speed_2:
            return pos_1 == pos_2
        if speed_1 > speed_2 and pos_1 > pos_2 or speed_1 < speed_2 and pos_1 < pos_2:
            return False

        time_needed = (pos_1 - pos_2) / (speed_2 - speed_1)

        return pos_1 + time_needed * speed_1 <= self.target

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        self.target = target

        cars_by_position = sorted(zip(position, speed), key=lambda x: x[0])

        fleets = 0
        stack = []

        for curr_pos, curr_speed in cars_by_position:
            fleets += 1

            while len(stack) > 0 and self.check_will_intersect(curr_pos, curr_speed, *stack[-1]):
                fleets -= 1
                stack.pop()
        
            stack.append((curr_pos, curr_speed))

        return fleets