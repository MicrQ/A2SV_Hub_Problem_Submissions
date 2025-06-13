# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        ins = defaultdict(int)
        outs = defaultdict(int)

        for node, edge in trust:
            ins[edge] += 1
            outs[node] += 1

        for person, trusts in ins.items():
            if trusts == n - 1 and outs[person] == 0:
                return person

        return -1
