# solution 1 (can't not pass)
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_sum_pair = inf
        n = len(nums)

        for perm in itertools.permutations(nums):
            curr_pair_sum = -inf

            for i in range(0, n, 2):
                tmp = perm[i] + perm[i+1]
                curr_pair_sum = max(curr_pair_sum, tmp)

            max_sum_pair = min(max_sum_pair, curr_pair_sum)

        return max_sum_pair

# solution 2
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum_pair = -inf
        for i in range(len(nums)//2):
            tmp = nums[i] + nums[-i-1]
            max_sum_pair = max(tmp, max_sum_pair)

        return max_sum_pair