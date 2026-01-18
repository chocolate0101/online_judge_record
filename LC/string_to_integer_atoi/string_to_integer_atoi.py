# link of the question: https://leetcode.com/problems/string-to-integer-atoi/description/

# solution 1
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        ans = 0
        is_read = 0
        for chr in s:
            if chr.isdigit():
                ans *= 10
                ans += int(chr)
                if not is_read:
                    is_read = 1
            else:
                if is_read:
                    break
                else:
                    if chr == "+":
                        sign = 1
                        is_read = 1
                    elif chr == "-":
                        sign = -1
                        is_read = 1
                    elif chr == " ":
                        continue
                    else:
                        break
        min = -(2 ** 31)
        max = (2 ** 31) - 1
        ans *= sign
        if ans >= max:
            return max
        elif ans <= min:
            return min
        return ans
    
# solution 2
class Solution:
    def myAtoi(self, s: str) -> int:
        new_string = s.lstrip()
        if not new_string:
            return 0
        
        sign = 1
        index = 0
        if new_string[0] == "-":
            sign = -1
        elif new_string[0] == "+":
            sign = 1
        index += 1

        num = 0
        while index < len(new_string) and new_string[index].isdigit():
            num *= 10
            num += int(new_string[index])
            index += 1

        INT_MIN = -(2 ** 31)
        INT_MAX = (2 ** 31) - 1
        if num <= INT_MIN:
            return INT_MIN
        elif num >= INT_MAX:
            return INT_MAX
        return num

"""

"""