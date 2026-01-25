class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        min_diff = inf
        for i in range(len(nums)-k+1):
            tmp = nums[i+k-1] - nums[i]
            if tmp < min_diff:
                min_diff = tmp

        return min_diff