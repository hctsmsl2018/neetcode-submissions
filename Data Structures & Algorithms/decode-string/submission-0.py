class Solution:
    def decode_recursively(self):
        decoded_parts = []

        while self.counter != len(self.s) and self.s[self.counter] != "]":
            if self.s[self.counter].isdigit():
                num_repititions = 0

                while self.s[self.counter] != "[":
                    num_repititions = num_repititions * 10 + int(self.s[self.counter])
                    self.counter += 1

                self.counter += 1

                decoded_parts.append(num_repititions * self.decode_recursively())

                self.counter += 1
            else:
                decoded_parts.append(self.s[self.counter])
                self.counter += 1

        return "".join(decoded_parts)

    def decodeString(self, s: str) -> str:
        self.counter = 0
        self.s = s

        return self.decode_recursively()