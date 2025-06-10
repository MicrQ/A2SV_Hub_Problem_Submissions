# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.min_unfair = float('inf')
        self.n = len(cookies)
        self.kids = [0] * k

        self.backtrack(cookies, 0, k)
        return self.min_unfair

    def backtrack(self, cookies, idx, k):
        if idx >= self.n:
            self.min_unfair = min(self.min_unfair, max(self.kids))
            return

        if max(self.kids) >= self.min_unfair:
            return

        for i in range(0, k):
            self.kids[i] += cookies[idx]
            self.backtrack(cookies, idx + 1, k)
            self.kids[i] -= cookies[idx]