# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        remaining_asteroids = []
        for asteroid in asteroids:

            # looping on the remaining asteroids
            while remaining_asteroids and asteroid < 0 and  remaining_asteroids[-1] > 0:
                if -asteroid == remaining_asteroids[-1]:
                    remaining_asteroids.pop()
                    break

                elif -asteroid > remaining_asteroids[-1]:
                    remaining_asteroids.pop()
                    continue

                else:
                    break

            else:
                remaining_asteroids.append(asteroid)

        return remaining_asteroids
