class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        final_asteroids = [] # 8, 

        for i in asteroids:
            if len(final_asteroids) == 0 or i > 0:
                final_asteroids.append(i)
            else:
                abs_i = abs(i)
                same_size_last_asteroid = False

                while len(final_asteroids) > 0 and not same_size_last_asteroid and 0 < final_asteroids[-1] <= abs_i:
                    same_size_last_asteroid = final_asteroids[-1] == abs_i
                    final_asteroids.pop()

                if not same_size_last_asteroid and (len(final_asteroids) == 0 or final_asteroids[-1] < 0):
                    final_asteroids.append(i)

        return final_asteroids
