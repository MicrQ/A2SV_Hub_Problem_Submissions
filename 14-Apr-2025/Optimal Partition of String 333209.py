# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:

        count = 1
        substring = set()

        for char in s:
            if char in substring:
                count += 1
                substring.clear()

            substring.add(char)

        return count
