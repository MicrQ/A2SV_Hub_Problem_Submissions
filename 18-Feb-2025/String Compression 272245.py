# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        left, right = 0, 0
        n = len(chars)

        while right < n:
            char = chars[right]
            count = 0

            # counting frequency of a char
            while right < n:
                if chars[right] == char:
                    count += 1
                    right += 1
                else:
                    break

            chars[left] = char
            left += 1

            str_count = str(count)
            if count > 1 and count >= 10:
                for char_count in str_count:
                    chars[left] = char_count
                    left += 1

            elif count > 1:
                chars[left] = str_count
                left += 1

        return left
