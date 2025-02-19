# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        friends = [num for num in range(1, n + 1)]

        i = 0

        # looping on friends and removing the kth player until one is left
        while len(friends) > 1:
            i = (i + k - 1) % len(friends)
            friends.pop(i)

        return friends[0]
