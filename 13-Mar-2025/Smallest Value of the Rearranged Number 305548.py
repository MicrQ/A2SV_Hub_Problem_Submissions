# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        
        is_ngtv = num < 0
        nums = list(str(num)[1:] if is_ngtv else str(num))

        if is_ngtv:
            nums.sort(reverse=True)
            new_num = int(''.join(nums))

            return -new_num

        nums.sort()
        
        # replace leading zero with the smallest non-zero
        i = 1
        while nums[0] == '0' and i < len(nums):
            if nums[i] != '0':
                nums[0], nums[i] = nums[i], nums[0]
                break

            i += 1

        return int(''.join(nums))
