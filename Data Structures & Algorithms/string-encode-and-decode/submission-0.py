class Solution:

    def encode(self, strs: List[str]) -> str:
        concat_elements = (str(len(strs)),) + tuple(str(len(s)) for s in strs) + ("".join(strs),)
        return ",".join(concat_elements)

    def decode(self, s: str) -> List[str]:
        num_elements, lengths_and_contents = s.split(",", maxsplit=1)
        lengths_and_contents_split = lengths_and_contents.split(",", maxsplit=int(num_elements))
        indexing_start = 0
        decoded = []

        for i in islice(lengths_and_contents_split, len(lengths_and_contents_split) - 1):
            curr_length = int(i)
            decoded.append(lengths_and_contents_split[-1][indexing_start:indexing_start + curr_length])
            indexing_start += curr_length

        return decoded