# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)

        steaks = defaultdict(int)

        for num in nums:

            # calculate the square of num and check if it exists
            sqr = num ** 2
            steaks[num] = steaks[sqr] + 1

        result = max(steaks.values())

        return result if result > 1 else -1