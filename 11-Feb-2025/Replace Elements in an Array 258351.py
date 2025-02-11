# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        # creating value, index pair of the nums list
        nums_idx = {num: idx for idx, num in enumerate(nums)}

        # looping through the operations and replacing nums[i] with
        #   its latest value
        for num, replace in operations:

            num_idx = nums_idx[num]
            
            # replace nums[num_idx] to its new value
            nums[num_idx] = replace

            # add the new value as key and its index as value to the dict
            nums_idx[replace] = num_idx

            # removing the old num, index pair for space optimization
            del nums_idx[num]

        return nums
