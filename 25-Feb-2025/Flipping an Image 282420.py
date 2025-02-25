# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        n = len(image)

        # reverseing the rows
        for row in image:
            row.reverse()

        # flipping all bits
        for row in range(n):
            for col in range(n):

                image[row][col] ^= 1

        return image