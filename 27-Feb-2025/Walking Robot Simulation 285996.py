# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obs_set = {(i, j) for i, j in obstacles}
        max_distance = 0
        pos = 0
        positions = [
            (0, 1), # North
            (1, 0), # East
            (0, -1), # South
            (-1, 0) # West
        ]
        x, y = 0, 0

        # looping through the commands to move the robot
        for cmd in commands:
            if cmd == -1:
                pos = (pos + 1) % 4 # looping infinitely in one direction
            elif cmd == -2:
                pos = (pos - 1) % 4

            else:
                while cmd > 0:
                    if (x + positions[pos][0], y + positions[pos][1]) in obs_set:
                        break

                    x += positions[pos][0]
                    y += positions[pos][1]

                    max_distance = max(max_distance, x**2 + y**2)
                    cmd -= 1

        return max_distance
