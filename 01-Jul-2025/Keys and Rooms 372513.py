# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlocked = [False] * len(rooms)
        queue = deque([0])
        visited = set()

        while queue:
            room = queue.popleft()
            unlocked[room] = True
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)

        return all(unlocked)