# link of the question: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/

# solution 1
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count_security_device = []
        total_beam = 0
        for i in range(len(bank)):
            count_device = sum( map(int, list(bank[i]) ) )
            count_security_device.append(count_device)

        for i in range(len(count_security_device)-1):
            if count_security_device[i] != 0 and count_security_device[i+1] != 0:
                total_beam += count_security_device[i] * count_security_device[i+1]
            else:
                for j in range(i+1, len(count_security_device)):
                    if count_security_device[j] != 0:
                        total_beam += count_security_device[i] * count_security_device[j]
                        break

        return total_beam
    
# solution 2
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        previous_row_device = 0
        total_beam = 0
        for i in range(len(bank)):
            current_row_device = sum( map(int, list(bank[i]) ) )
            if current_row_device != 0:
                total_beam += current_row_device * previous_row_device
                previous_row_device = current_row_device

        return total_beam
    
# solution 3
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        previous_row_device = 0
        total_beam = 0
        for row in bank:
            current_row_device = row.count("1")
            if current_row_device != 0:
                total_beam += current_row_device * previous_row_device
                previous_row_device = current_row_device

        return total_beam
    
"""
- suppose bank is size N*M

- time complexity of solution 1: O(N*N)
    - first for loop need to check the element of all rows => O(N*M)
    - second for need to check all the counting result of count_security_device => O(N*N)
        - in worst case, only first has security device, then every row need to repeat checking all the rest row 
    - Therefore, total = O(N*M) + O(N*N) = O(N*N)

- time complexity of solution 2: O(N*M)
    - need to count the number of 1 in each row
    - each row need O(M) and there are N row => O(N*M)
    - Therefore, total = O(N*M)

- time complexity of solution 3: O(N*M)
    - need to count the number of 1 in each row
    - each row need O(M) and there are N row => O(N*M)
    - Therefore, total = O(N*M)

- faster way to count the number of 1 in each row
    - solution 2 uses sum( map(int, list(bank)) )
    - solution 3 uses row.count("1")
    - the way that solution 2 use has many step need to do, however the way that solution 3 is a method that implement in C
    - Therefore, it's faster than solution 2
"""

"""
- space complexity of solution 1: O(N)
    - first for loop need a list to store the counting result of each row => O(N)
    - need one variable to store the total beams => O(1)
    - Therefore, total = O(N) + O(1) = O(N)

- space complexity of solution 2: O(1)
    - need two variable to store the total beams => O(1)

- space complexity of solution 3: O(1)
    - need two variable to store the total beams => O(1)
"""

"""
- new method `row.count(target, start, end)`
    - it will count the number of string that same as the target
    - should be careful that it only count non-overlapping
Ex:
str1 = "aaaaa"
print(str1.count("aa")) # output = 2

str2 = "hello world hello world"
print(str2.count("hello")) # output = 2
print(str2.count("hello", 0, 10)) # output = 1
print(str2.count("hello", 10)) # output = 1 (count from 10th char to the end)
"""