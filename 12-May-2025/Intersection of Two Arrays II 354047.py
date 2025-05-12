# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_frq = Counter(nums1)
        result = []

        for num in nums2:
            if num1_frq[num] > 0:
                result.append(num)
                num1_frq[num] -= 1

        return result
        