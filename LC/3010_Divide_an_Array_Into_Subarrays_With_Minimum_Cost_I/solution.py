class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_1, min_2 = inf, inf
        for i in range(1, len(nums)):
            if nums[i] < min_1:
                min_2 = min_1
                min_1 = nums[i]
            elif nums[i] < min_2:
                min_2 = nums[i]

        return nums[0] + min_1 + min_2