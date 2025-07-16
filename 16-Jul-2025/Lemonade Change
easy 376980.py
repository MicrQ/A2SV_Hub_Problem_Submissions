# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        price = 5
        fives, tens = 0, 0

        for bill in bills:
            if bill == 5:
                fives += 1
            if bill == 10:
                tens += 1

            change = bill - price

            if change == 5:
                if fives:
                    fives -= 1
                else:
                    return False

            elif change == 15:
                if fives and tens:
                    fives, tens = fives - 1, tens - 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False

        return True
