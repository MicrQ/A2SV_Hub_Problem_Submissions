# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        res = []

        # building the dependency graph
        for recipe, ings in zip(recipes, ingredients):
            for ing in ings:
                graph[ing].append(recipe)
                in_degree[recipe] += 1

        # kahn's algorithm :)
        queue = deque(supplies)
        recipe_set = set(recipes)

        while queue:
            item = queue.popleft()

            if item in recipe_set:
                res.append(item)

            for nei in graph[item]:
                in_degree[nei] -= 1

                if in_degree[nei] == 0:
                    queue.append(nei)

        return res
