# link of the question: https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_set = set(nums1)
        num2_set = set(nums2)
        ans = list(num1_set.intersection(num2_set))

        return ans