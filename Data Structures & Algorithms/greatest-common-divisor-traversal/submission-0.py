'''class UnionFind:
    def __init__(self, nums, factors):
        self._items = {n:f for n, f in zip(nums, factors)}
        self._groups = set(nums)

    def union(self, n1, n2):
        if len(self._items[n2] & self._items[n1][i]) > 0:
            self._items[n1] |= self._items[n2]
            self._items[n2] = n1
            self._groups.remove(n2)

            return True
        else:
            return False

    def find(self, n):
        curr_num = n

        while not isinstance(self._items[curr_num], dict):
            curr_num = self._items[curr_num]

        self._items[n] = curr_num

        return curr_num

    def get_groups(self):
        return groups'''

class Solution:
    def _prime_factorize(self, n):
        factors = set()

        while n % 2 == 0:
            n //= 2
            factors.add(2)

        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                n //= i
                factors.add(i)

            if n == 1:
                break

        if n != 1:
            factors.add(n)

        return factors

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if nums == [1]:
            return True

        nums_set = set(nums)

        if 1 in nums_set:
            return False

        prev_not_merged_prime_factors = [self._prime_factorize(n) for n in nums_set]
        all_factors = prev_not_merged_prime_factors.pop()

        while True:
            curr_not_merged_prime_factors = []

            for factors in prev_not_merged_prime_factors:
                if len(factors & all_factors) > 0:
                    all_factors |= factors
                else:
                    curr_not_merged_prime_factors.append(factors)

            if len(curr_not_merged_prime_factors) == 0:
                return True
            elif len(prev_not_merged_prime_factors) == len(curr_not_merged_prime_factors):
                return False
            
            prev_not_merged_prime_factors = curr_not_merged_prime_factors

        '''graph = defaultdict(set)

        for i in range(len(prime_factors) - 1):
            for j in range(i + 1, len(prime_factors)):
                if len(prime_factors[i] & prime_factors[j]) > 0:
                    graph[i].add(j)
                    graph[j].add(i)

        queue = deque((0,))
        visited = {0}

        while len(queue) != 0:
            curr_num = queue.popleft()
        
            for i in graph[curr_num]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        return len(visited) == len(nums_set)'''