from math import inf

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flights_graph = defaultdict(set)

        for f, t, p in flights:
            flights_graph[f].add((t, p))

        prev_cheapest_prices = {src: 0} # {1: 100}
        cheapest_price_to_dest = inf

        for _ in range(k + 1):
            new_cheapest_prices = defaultdict(lambda: inf) # {2: 200, 3: 700}

            for city, cheapest_price in prev_cheapest_prices.items():
                for to, price in flights_graph[city]:
                    new_cheapest_prices[to] = min(cheapest_price + price, new_cheapest_prices[to])

            cheapest_price_to_dest = min(cheapest_price_to_dest, new_cheapest_prices[dst])
            prev_cheapest_prices = new_cheapest_prices

        return cheapest_price_to_dest if cheapest_price_to_dest != inf else -1