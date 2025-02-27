# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)

        if n < 3:
            return 0

        total = 0

        for i in range(n):
            boomrangs = defaultdict(int)

            for j in range(n):

                # making sure not to use one point twice
                if i == j:
                    continue

                distance = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                boomrangs[distance] += 1

            # summing total boomrangs
            for val in boomrangs.values():
                total += val * (val - 1)

        return total