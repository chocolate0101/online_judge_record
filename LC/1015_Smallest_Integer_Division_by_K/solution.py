# link of the problem: https://leetcode.com/problems/smallest-integer-divisible-by-k

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        ans, length = 1, 1
        while True:
            if ans % k == 0:
                return length
            else:
                ans = ans * 10 + 1
                length += 1