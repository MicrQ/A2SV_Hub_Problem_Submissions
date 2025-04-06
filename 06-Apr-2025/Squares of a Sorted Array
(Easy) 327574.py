# Problem: Squares of a Sorted Array
(Easy) - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """ using two pointers. with O(n) auxilary space though """
        n = len(nums)
        left, right = 0, n - 1
        idx = n - 1
        answer = [0 for _ in range(n)]

        while left <= right:

            sqr_left = nums[left] ** 2
            sqr_right = nums[right] ** 2

            if sqr_left > sqr_right:
                answer[idx] = sqr_left
                left += 1

            else:
                answer[idx] = sqr_right
                right -= 1

            idx -= 1

        return answer


        # # Solving with O(nlog(n)). just for now
        # n = len(nums)

        # for i in range(n):
        #     nums[i] *= nums[i]

        # nums.sort()

        # return nums