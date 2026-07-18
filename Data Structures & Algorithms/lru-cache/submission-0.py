VALUE = 0
NODE = 1

class Node:
    def __init__(self, key, prev_node=None, next_node=None):
        self.key = key
        self.prev_node = prev_node
        self.next_node = next_node

class LRUCache:

    def __init__(self, capacity: int):
        self._key_to_value_node = {}
        self._least_recently_used = None
        self._most_recently_used = None
        self._capacity = capacity
        self._length = 0

    def get(self, key: int) -> int:
        if key in self._key_to_value_node:
            value, key_node = self._key_to_value_node[key]

            self._bring_to_front(key_node)
            
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._key_to_value_node:
            self._key_to_value_node[key][VALUE] = value

            self._bring_to_front(self._key_to_value_node[key][NODE])
        else:
            if self._capacity == self._length:
                del self._key_to_value_node[self._least_recently_used.key]

                self._least_recently_used = self._least_recently_used.next_node

                if self._length == 1:
                    self._most_recently_used = None
            else:
                self._length += 1

            new_node = Node(key, prev_node=self._most_recently_used)

            if self._least_recently_used is None:
                self._least_recently_used = new_node
            else:
                self._most_recently_used.next_node = new_node

            self._most_recently_used = new_node

            self._key_to_value_node[key] = [value, new_node]

    def _bring_to_front(self, node):
        if self._most_recently_used is not node:
            if self._least_recently_used is node:
                self._least_recently_used = self._least_recently_used.next_node
                
            prev_node = node.prev_node
            next_node = node.next_node
            
            if prev_node is not None:
                prev_node.next_node = next_node

            if next_node is not None:
                next_node.prev_node = prev_node

            self._most_recently_used.next_node = node
            node.prev_node = self._most_recently_used
            node.next_node = None
            self._most_recently_used = node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)