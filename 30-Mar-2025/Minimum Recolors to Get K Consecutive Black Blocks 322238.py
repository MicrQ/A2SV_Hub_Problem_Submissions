# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        n = len(blocks)

        whites = 0

        # creating the initial window
        for i in range(k):
            if blocks[i] == 'W':
                whites += 1

        # looking for the minimum recolored window
        left = 0
        curr_whites = whites
        for right in range(k, n):

            # if the expanded window contains another 'W'
            if blocks[right] == 'W':
                curr_whites += 1

            # if the shrinked part is 'W'
            if blocks[left] == 'W':
                curr_whites -= 1

            whites = min(whites, curr_whites)
            left += 1

        return whites