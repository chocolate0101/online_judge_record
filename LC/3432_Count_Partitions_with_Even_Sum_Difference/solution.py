# solution 1
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count, left= 0, 0
        right = sum(nums)
        for i in range(len(nums)-1):
            left += nums[i]
            right -= nums[i]
            if abs(left - right) % 2 == 0:
                count += 1

        return count
    
# solution 2
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0