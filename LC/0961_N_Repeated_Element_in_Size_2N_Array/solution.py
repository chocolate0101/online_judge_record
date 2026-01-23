# solution 1
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                return num
            d[num] = 1

# solution 2 (best solution)
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2):
            if nums[i] == nums[i+1] or nums[i] == nums[i+2]:
                return nums[i]
        
        return nums[-1]