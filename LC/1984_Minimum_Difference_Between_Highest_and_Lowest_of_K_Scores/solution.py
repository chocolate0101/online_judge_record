# solution 1
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        self.min_diff = inf
        n = len(nums)

        def backtrack(start_index, curr_comb):
            if len(curr_comb) == k:
                curr_min = max(curr_comb) - min(curr_comb)
                self.min_diff = min(self.min_diff, curr_min)
                return
            
            for i in range(start_index, n):
                curr_comb.append(nums[i])
                backtrack(i+1, curr_comb)
                curr_comb.pop()

        backtrack(0, [])
        return self.min_diff

# solution 2
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