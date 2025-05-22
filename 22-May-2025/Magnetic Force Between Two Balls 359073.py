# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        # helper here
        def forceFinder(force):
            balls = 1
            prev_pos = position[0]

            for pos in position[1:]:
                if prev_pos + force <= pos:
                    prev_pos = pos
                    balls += 1

            return balls >= m


        left, right = 0, (position[-1] - position[0])
        max_force = 0

        while left <= right:
            mid = left + (right - left) // 2

            if forceFinder(mid):
                max_force = max(max_force, mid)
                left = mid + 1
            else:
                right = mid - 1

        return max_force