class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # 1, 2, 2, 3

        left = 0 # 1
        right = len(people) - 1 # 0

        boats = 0 # 2
        curr_people = 0
        curr_tot_weight = 0 # 2

        while left <= right:
            if curr_tot_weight + people[right] <= limit and curr_people < 2:
                curr_tot_weight += people[right]
                right -= 1
                curr_people += 1
            elif curr_tot_weight + people[left] <= limit and curr_people < 2:
                curr_tot_weight += people[left]
                left += 1
                curr_people += 1
            else:
                boats += 1
                curr_people = 0
                curr_tot_weight = 0
                
        if curr_tot_weight > 0:
            boats += 1

        return boats