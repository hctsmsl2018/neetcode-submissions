# RRRDDRRRRDDDDDDRRDDDDDDDDDDDDRRRRR

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        num_radient = 0 # 0
        num_dire = 0 # 1
        num_radient_skips = 0 # 
        num_dire_skips = 0 # 0

        for s in senate:
            if s == "R":
                num_radient += 1
            elif s == "D":
                num_dire += 1

        if num_radient == 0:
            return "Dire"

        if num_dire == 0:
            return "Radiant"

        senate_queue = deque(senate)

        while True:
            curr_senator = senate_queue.popleft()

            if curr_senator == "R":
                if num_radient_skips > 0:
                    num_radient_skips -= 1
                else:
                    num_dire -= 1

                    if num_dire == 0:
                        return "Radiant"
                        
                    num_dire_skips += 1

                    senate_queue.append(curr_senator)
            elif curr_senator == "D":
                if num_dire_skips > 0:
                    num_dire_skips -= 1
                else:
                    num_radient -= 1

                    if num_radient == 0:
                        return "Dire"

                    num_radient_skips += 1

                    senate_queue.append(curr_senator)