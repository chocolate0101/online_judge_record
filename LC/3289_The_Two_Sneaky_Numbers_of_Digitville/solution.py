# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_count = Counter(nums)

        return [key for key, value in num_count.items() if value == 2]
        