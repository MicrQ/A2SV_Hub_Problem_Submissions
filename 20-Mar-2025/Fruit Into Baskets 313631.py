# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        left = 0
        max_subarray = 0
        types = defaultdict(int)

        for right in range(len(fruits)):

            # expanding window to right
            fruit = fruits[right]
            types[fruit] += 1

            # checking if more than two type of fruits is in the window
            if len(types) > 2:

                if types[fruits[left]] > 1:
                    # if the count is more than 1
                    types[fruits[left]] -= 1
                else:
                    del types[fruits[left]]

                left += 1

            max_subarray = max(max_subarray, right - left + 1)

        return max_subarray