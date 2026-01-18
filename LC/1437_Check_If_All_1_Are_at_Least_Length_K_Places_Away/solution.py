# link of the question: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 in nums:
            prev_idx = nums.index(1)
        else:
            return True

        for i in range(prev_idx+1, len(nums)):
            if nums[i] == 1:
                idx = i
                if idx - prev_idx - 1 < k:
                    return False
                prev_idx = idx
        return True