# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:

        roman_nums = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            40: 'XL',
            90: 'XC',
            50: 'L',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        roman_num = ''

        # dividing num by each key of the hashmap and calculating its roman value
        for int_val in sorted(roman_nums.keys(), reverse=True):

            # number of reps for roman num
            repeats = num // int_val
            roman_num += roman_nums[int_val] * repeats

            # subtracting the added sign value
            num -= int_val * repeats

        return roman_num
