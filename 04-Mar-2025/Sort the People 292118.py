# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        # using bubble sort
        n = len(names)

        for i in range(n):
            for j in range(n - i - 1):

                if heights[j] < heights[j + 1]:
                    # swap
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]

        return names




        # # height_name_pairs: used to store height: name pairs
        # # looping through both lists and storing the
        # height_name_pairs = {heights[i]: names[i] for i in range(len(names))}

        # return [height_name_pairs[height] for height in sorted(
        #     height_name_pairs.keys(), reverse=True)]
