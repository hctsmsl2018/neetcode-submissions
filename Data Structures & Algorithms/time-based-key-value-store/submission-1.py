from bisect import bisect_left

class TimeMap:

    def __init__(self):
        self._dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        key_list = self._dict[key]
        index = bisect_left(key_list, timestamp, key=lambda x: x[0])

        if not key_list or index == 0 and timestamp < key_list[index][0]:
            return ''

        return key_list[index - (index == len(key_list) or not key_list[index][0] == timestamp)][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)