# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        current = []
        
        def backtrack(idx):
            if idx == n:
                return len(current) >= 2

            # spliting and checking for all possibilities
            for i in range(idx, n):
                val = int(s[idx:i + 1])
                # append and backtrack only if the val is less by 1 from the prev
                if len(current) == 0 or val == current[-1] - 1:
                    current.append(val)
                    if backtrack(i + 1): # checked all or valid found
                        return True

                    current.pop()

            return False

        return backtrack(0)
                    