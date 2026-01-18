# solution 1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 0
        for i in range(len(digits)):
            integer += digits[i]
            integer *= 10
        
        integer_list = list(map(int, str(integer // 10 + 1)))

        return integer_list

# solution 2 (best solution)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
    
# solution 3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int("".join(str(digit) for digit in digits)) + 1
        return list(map(int, str(integer)))
