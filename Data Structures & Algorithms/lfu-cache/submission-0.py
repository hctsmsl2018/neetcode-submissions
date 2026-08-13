class Node:
    def __init__(self, val):
        self.val = val
        self.prev_node = None
        self.next_node = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def add(self, node):
        if self.start is None:
            self.start = node
            self.end = node
        else:
            self.end.next_node = node
            node.prev_node = self.end
            self.end = node

        self.length += 1

    def remove(self):
        start = self.start
        self.remove_specific_node(self.start)
        return start

    def empty(self):
        return self.length == 0

    def remove_specific_node(self, node):
        prev_node = node.prev_node
        next_node = node.next_node

        if prev_node is None:
            self.start = next_node
        else:
            prev_node.next_node = next_node
            node.prev_node = None

        if next_node is None:
            self.end = prev_node
        else:
            next_node.prev_node = prev_node
            node.next_node = None

        self.length -= 1

class LFUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._fewest_uses = 0
        self._most_recent_by_num_uses = defaultdict(DoublyLinkedList)
        self._node_info = {}

    def get(self, key: int) -> int:
        if key in self._node_info:
            self._update_counter(key)

            return self._node_info[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._node_info:
            self._update_counter(key)
            self._node_info[key][0] = value
        else:
            if len(self._node_info) == self._capacity:
                removed = self._most_recent_by_num_uses[self._fewest_uses].remove()

                if self._most_recent_by_num_uses[self._fewest_uses].empty():
                    del self._most_recent_by_num_uses[self._fewest_uses]

                del self._node_info[removed.val]

            self._fewest_uses = 0

            node = Node(key)
            self._node_info[key] = [value, node, 0]
            self._most_recent_by_num_uses[0].add(node)

    def _update_counter(self, key):
        _, node, uses = self._node_info[key]

        self._most_recent_by_num_uses[uses].remove_specific_node(node)

        if self._most_recent_by_num_uses[uses].empty():
            del self._most_recent_by_num_uses[uses]

        if self._fewest_uses not in self._most_recent_by_num_uses:
            self._fewest_uses += 1

        self._node_info[key][2] += 1

        self._most_recent_by_num_uses[self._node_info[key][2]].add(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)