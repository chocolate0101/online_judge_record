# link of the question: https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description/

# solution 1:
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        one_count = nums.count(1)
        if one_count != 0:
            return len(nums) - one_count
        
        min_create_one = inf
        for i in range(len(nums)-1):
            current_gcd = nums[i]
            for j in range(i+1, len(nums)):
                current_gcd = gcd(current_gcd, nums[j])

                if current_gcd == 1:
                    min_create_one = min(j-i, min_create_one)

        if min_create_one == inf:
            return -1
        else:
            return min_create_one + len(nums) - 1