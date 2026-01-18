# link of the question: https://leetcode.com/problems/binary-prefix-divisible-by-5/description/

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        tmp = 0
        for num in nums:
            tmp += num
            if tmp % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)

            tmp *= 2

        return ans