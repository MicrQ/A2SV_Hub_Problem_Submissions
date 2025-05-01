# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mono_stack = []
        s_frqs = Counter(s)
        seen = set()

        for char in s:
            if char in seen:
                s_frqs[char] -= 1
                continue

            while mono_stack and mono_stack[-1] > char and s_frqs[mono_stack[-1]] > 0:
                seen.remove(mono_stack.pop())

            mono_stack.append(char)
            seen.add(char)
            s_frqs[char] -= 1

        return ''.join(mono_stack)
