# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) - 1

        while left < right:

            if numbers[left] + numbers[right] == target:
                # 1 indexed result
                return [left + 1, right + 1]

            elif numbers[left] + numbers[right] < target:
                left += 1

            else:
                right -= 1

        return []
