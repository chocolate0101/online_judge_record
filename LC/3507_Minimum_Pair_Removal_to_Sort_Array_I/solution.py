class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        total_operation = 0
        while True:
            if sorted(nums) == nums:
                break
            
            min_sum = inf
            min_index = 0
            for i in range(len(nums)-1):
                tmp = nums[i] + nums[i+1]
                if tmp < min_sum:
                    min_sum = tmp
                    min_index = i

            nums[min_index] = min_sum
            del nums[min_index+1]
            total_operation += 1

        return total_operation