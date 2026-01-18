# link of the question: https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""

        if num >= 1000:
            M = num // 1000
            num %= 1000
            ans += 'M' * M
        
        if num >= 900:
            ans += 'CM'
            num %= 100
        elif 500 <= num < 900:
            tmp = num // 100 - 5
            ans += 'D' + 'C' * tmp
            num %= 100
        elif num >= 400:
            ans += 'CD'
            num %= 100
        elif 100 <= num < 400:
            tmp = num // 100
            ans += 'C' * tmp
            num %= 100

        if num >= 90:
            ans += 'XC'
            num %= 10
        elif 50 <= num < 90:
            tmp = num // 10 - 5
            ans += 'L' + 'X' * tmp
            num %= 10
        elif num >= 40:
            ans += 'XL'
            num %= 10
        elif 10 <= num < 40:
            tmp = num // 10
            ans += 'X' * tmp
            num %= 10

        if num == 9:
            ans += 'IX'
        elif 5 <= num < 9:
            tmp = num - 5
            ans += 'V' + 'I' * tmp
        elif num == 4:
            ans += "IV"
        elif 1 <= num < 4:
            ans += 'I' * num

        return ans 