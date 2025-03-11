# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """ the pancake sort itself """

        """ start traversing the list starting from the end
            find the max unsorted value, move it to the front and
            finally to its correct position
        """
        n = len(arr)
        result = []

        for i in range(n - 1, -1, -1):
            max_ = i

            # find the max unsorted element
            for j in range(i, -1, -1):
                if arr[j] > arr[max_]:
                    max_ = j

            if max_ != i:
                self.flipper(arr, max_)
                self.flipper(arr, i)

                result.append(max_ + 1)
                result.append(i + 1)

        return result


    def flipper(self, arr: List[int], end: int) -> None:
        """ helper for the pancake sort method """

        start = 0

        while start < end:

            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
