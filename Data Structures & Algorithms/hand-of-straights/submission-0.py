class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        reverse_sorted_hand_counts = sorted(Counter(hand).items(), reverse=True) # [(8, 1), (7, 1), (6, 1)]

        while len(reverse_sorted_hand_counts) != 0:
            return_to_all_counts = [] # 
            seq_start = reverse_sorted_hand_counts[-1][0]

            for i in range(seq_start, seq_start + groupSize):
                if len(reverse_sorted_hand_counts) == 0:
                    return False

                curr_element, count = reverse_sorted_hand_counts.pop()

                if curr_element != i:
                    return False

                if count > 1:
                    return_to_all_counts.append((curr_element, count - 1))

            reverse_sorted_hand_counts.extend(reversed(return_to_all_counts))

        return True