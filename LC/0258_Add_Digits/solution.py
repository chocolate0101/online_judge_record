# link of the question: https://leetcode.com/problems/add-digits/description/

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum_digit = 0
            while num > 0:
                sum_digit += num % 10
                num //= 10
            num = sum_digit

        return num