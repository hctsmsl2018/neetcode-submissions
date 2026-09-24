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

        eliminated = set()

        i = 0

        while True:
            if i in eliminated:
                i = (i + 1) % len(senate)
                continue

            if senate[i] == "R":
                if num_radient_skips > 0:
                    num_radient_skips -= 1
                    eliminated.add(i)
                else:
                    num_dire -= 1

                    if num_dire == 0:
                        return "Radiant"
                        
                    num_dire_skips += 1
            elif senate[i] == "D":
                if num_dire_skips > 0:
                    num_dire_skips -= 1
                    eliminated.add(i)
                else:
                    num_radient -= 1

                    if num_radient == 0:
                        return "Dire"

                    num_radient_skips += 1

            i = (i + 1) % len(senate)