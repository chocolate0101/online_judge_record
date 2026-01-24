class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum_pair = []
        for i in range(len(nums)//2):
            tmp = nums[i] + nums[-i-1]
            max_sum_pair.append(tmp)

        return max(max_sum_pair)