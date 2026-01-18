# link of the question: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if not num % 3 == 0:
                count += 1

        return count