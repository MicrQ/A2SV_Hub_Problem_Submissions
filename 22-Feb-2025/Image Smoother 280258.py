# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        m = len(img)
        n = len(img[0])

        result = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):

                total = 0
                count = 0

                for cell_row in range(-1, 2):
                    for cell_col in range(-1, 2):

                        if 0 <= row + cell_row < m and 0 <= col + cell_col < n:
                            total += img[row + cell_row][col + cell_col]
                            count += 1

                result[row][col] = total // count

        return result


















        # tiring way
        # for row in range(m):


        #     for col in range(n):
        #         sum = 0
        #         count = 0
        #         sum += img[row][col]
        #         count += 1#C

        #         if col > 0:
        #             sum += img[row][col - 1]
        #             count += 1#L

        #             if row > 0:
        #                 sum += img[row - 1][col - 1]
        #                 count += 1#TL

        #             if row < m - 1:
        #                 sum += img[row + 1][col - 1]
        #                 count += 1#BL

        #         if col < n - 1:
        #             sum += img[row][col + 1]
        #             count += 1

        #         if row > 0:
        #             sum += img[row - 1][col]
        #             count += 1#T

        #             if col < n - 1:
        #                 sum += img[row - 1][col + 1]
        #                 count += 1#TR

        #         if row < m - 1:
        #             sum += img[row + 1][col]
        #             count += 1#B

        #             if col < n - 1:
        #                 sum += img[row + 1][col + 1]
        #                 count += 1#BR

        #         result[row][col] = sum // count

        # return result