class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        change = 0
        n = len(nums)

        if n < 4 or nums[0] >= nums[1]:
            return False
        
        for i in range(n-1):
            if change % 2 == 1 and nums[i] < nums[i+1]:
                change += 1
            elif change % 2 == 0 and nums[i] > nums[i+1]:
                change += 1
            elif nums[i] == nums[i+1]:
                return False

        return change == 2