# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        n = len(mat)
        max_1s = [0, 0]

        # just itrating throught the matrix and keeping count of 1s
        for row in range(n):
            
            count = 0
            for num in mat[row]:
                if num == 1:
                    count += 1

            if count > max_1s[1]:
                max_1s[0], max_1s[1] = row, count

        return max_1s
