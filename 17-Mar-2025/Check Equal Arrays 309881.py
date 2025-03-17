# Problem: Check Equal Arrays - https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

# User function Template for python3
from collections import Counter

class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        
        a_frq = Counter(a)
        b_frq = Counter(b)
        
        if len(a_frq) != len(b_frq):
            return False
            
        for a_key, a_val in a_frq.items():
            # checking if the elemetes have a same frequencey in both lists
            
            if b_frq.get(a_key) is None or b_frq.get(a_key) != a_val:
                return False
                
        return True