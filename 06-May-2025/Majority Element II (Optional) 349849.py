# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        bar = len(nums) // 3
        
        answer = []
        for num, frq in Counter(nums).items():
            if frq > bar:
                answer.append(num)

        return answer