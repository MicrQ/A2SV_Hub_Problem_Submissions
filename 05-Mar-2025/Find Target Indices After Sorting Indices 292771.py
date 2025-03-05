# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def binarySearch(self, left, right, arr, target, indices=[]):
        """ binary search implementation """

        if left > right:
            return

        mid = left + (right - left) // 2
        if arr[mid] == target:
            indices.append(mid)

            # checking if there are more than one nums equal to target
            self.binarySearch(left, mid - 1, arr, target, indices)
            self.binarySearch(mid + 1, right, arr, target, indices)

        # searching in the right half
        elif arr[mid] < target:
            self.binarySearch(mid + 1, right, arr, target, indices)

        # searching in left half
        else:
            self.binarySearch(left, mid - 1, arr, target, indices)

    
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        """ searching nums that are equal to target
            after sorting the list first.
        """
        nums.sort()
        indices = []

        self.binarySearch(0, len(nums) - 1, nums, target, indices)

        indices.sort()

        return indices