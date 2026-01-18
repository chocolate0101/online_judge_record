# link of the question: https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while True:
            if original in nums:
                original *= 2
            else:
                return original