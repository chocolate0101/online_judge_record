# link of the question: https://leetcode.com/problems/happy-number

# first try
class Solution:
    def isHappy(self, n: int) -> bool:
        n_str = str(n)
        digit_list = [int(digit) for digit in n_str]
        
        unique_num = set()
        while(1):
            sum = 0
            for i in range(len(digit_list)):
                sum += digit_list[i] ** 2

            if sum == 1:
                return True
            elif sum in unique_num:
                return False
            else:
                unique_num.add(sum)

            digit_list = [int(digit) for digit in str(sum)]
            
# more clear
class Solution:
    def isHappy(self, n: int) -> bool:
        unique_num = set()
        while(1):
            n = sum([int(digit) ** 2 for digit in str(n)])

            if n == 1:
                return True
            elif n in unique_num:
                return False
            else:
                unique_num.add(n)