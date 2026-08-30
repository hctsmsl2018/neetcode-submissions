class Solution:
    def _get_addresses_with_prefix(self, ind):
        if len(self._curr_address) == 4 and ind == len(self._s):
            self._all_addresses.append(".".join(self._curr_address))
        elif len(self._curr_address) != 4 and ind != len(self._s):
            if self._s[ind] == "0":
                self._curr_address.append("0")
                self._get_addresses_with_prefix(ind + 1)
                self._curr_address.pop()
            else:
                for i in range(ind + 1, min(ind + 4, len(self._s) + 1)):
                    curr_num = self._s[ind:i]

                    if 0 <= int(self._s[ind:i]) <= 255:
                        self._curr_address.append(curr_num)
                        self._get_addresses_with_prefix(i)
                        self._curr_address.pop()
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        self._s = s
        self._curr_address = []
        self._all_addresses = []

        self._get_addresses_with_prefix(0)

        return self._all_addresses