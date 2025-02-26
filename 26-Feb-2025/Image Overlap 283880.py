# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # memory for positions of 1's in img1 and img2
        n = len(img1)

        img1_1s = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        img2_1s = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        shift_count = defaultdict(int)

        for x1, y1 in img1_1s:
            for x2, y2 in img2_1s:

                shiftx, shifty = x2 - x1, y2 - y1
                shift_count[(shiftx, shifty)] += 1

        return max(shift_count.values(), default=0)

        






        # n = len(img1)
        # img2_1s = []

        # # looping through img2 and memorizing positions of 1's
        # for i in range(n):
        #     for j in range(n):

        #         if img2[i][j] == 1:
        #             img2_1s.append((i - 1, j - 1))

        # max_overlap = 0
        # # looping through the img1 and counting the max overlap
        # for row in range(n):
        #     for col in range(n):

        #         current_overlap = 0

        #         # counting image overlaps
        #         for x, y in img2_1s:
        #             row_x = row + x
        #             col_y = col + y

        #             if row_x < n and col_y < n and img1[row_x][col_y] == 1:
        #                 current_overlap += 1

        #         max_overlap = max(max_overlap, current_overlap)

        # return max_overlap
