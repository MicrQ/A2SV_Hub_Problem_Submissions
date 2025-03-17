# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        copy = arr[:]
        n = len(arr)

        i = 0
        for num in copy:

            if not i < n:
                break

            if num == 0 and i < n - 1:
                arr[i + 1], arr[i] = 0, 0
                i += 1

            elif num == 0:
                arr[i] = 0

            else:
                arr[i] = num

            i += 1


