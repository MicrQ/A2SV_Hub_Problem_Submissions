# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        # creating a hashmap for limits and color counts
        balls = defaultdict(int)
        colors = defaultdict(int)

        distincts = []

        
        for ball, color in queries:

            if balls[ball] > 0:

                colors[balls[ball]] -= 1
                if colors[balls[ball]] <= 0:
                    del colors[balls[ball]]

            balls[ball] = color
            colors[color] += 1

            distincts.append(len(colors))

        return distincts