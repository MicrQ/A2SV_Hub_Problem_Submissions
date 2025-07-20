# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # using two pointers
        left = 0
        right = len(height) - 1

        max_size = 0

        while left < right:
            # identify the min
            min_ = min(height[left], height[right])
            max_size = max(max_size, min_ * (right - left))

            if height[left] == min_:
                left += 1
            else:
                right -= 1

        return max_size