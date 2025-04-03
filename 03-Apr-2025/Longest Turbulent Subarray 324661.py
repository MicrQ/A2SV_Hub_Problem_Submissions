# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        n = len(arr)
        max_len = 1
        greater, less = 1, 1

        if n == 1:
            return 1

        for i in range(1, n):

            if arr[i] > arr[i - 1]:
                # the previouse was less than
                greater = less + 1
                less = 1

            elif arr[i] < arr[i - 1]:
                # the previouse was greater than
                less = greater + 1
                greater = 1

            else:
                # resetting when they are equal
                less = 1
                greater = 1
            

            max_len = max(max_len, greater, less)

        return max_len