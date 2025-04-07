# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        # using sliding window and counting number of odd numbers
        odds = 0
        left = 0
        count = 0
        nice_subarrays = 0

        for right in range(len(nums)):

            # expanding the window
            if nums[right] % 2 == 1:
                odds += 1
                count = 0

            while odds >= k:

                count += 1

                if nums[left] % 2 == 1:
                    odds -= 1

                left += 1

            nice_subarrays += count

        return nice_subarrays
