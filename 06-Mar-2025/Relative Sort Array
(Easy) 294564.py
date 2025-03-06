# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        arr1_frq = Counter(arr1)

        # now I can iterate through arr2 and create new list in its order
        i = 0
        for num in arr2:

            # now, I can modify arr1 accordingly
            for j in range(arr1_frq[num]):
                arr1[i] = num
                i += 1
                del arr1_frq[num] # removing it to know the leftovers

        for num in sorted(arr1_frq.keys()):
            # adding the leftovers to the end of arr1

            for j in range(arr1_frq[num]):
                arr1[i] = num
                i += 1
        return arr1