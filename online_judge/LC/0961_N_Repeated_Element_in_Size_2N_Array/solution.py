# solution 1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int("".join(str(digit) for digit in digits)) + 1
        return list(map(int, str(integer)))

# solution 2
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                return num
            d[num] = 1

# solution 3 (best solution)
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2):
            if nums[i] == nums[i+1] or nums[i] == nums[i+2]:
                return nums[i]
        
        return nums[-1]