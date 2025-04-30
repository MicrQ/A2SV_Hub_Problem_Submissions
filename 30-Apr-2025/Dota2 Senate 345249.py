# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rs_idx, ds_idx = deque(), deque()
        n = len(senate)

        for i in range(n):
            char = senate[i]
            if char == 'R':
                rs_idx.append(i)
            else:
                ds_idx.append(i)

        while rs_idx and ds_idx:
            ri, di = rs_idx.popleft(), ds_idx.popleft()

            if ri < di:
                rs_idx.append(ri + n)
            else:
                ds_idx.append(di + n)


        return 'Dire' if ds_idx else 'Radiant'