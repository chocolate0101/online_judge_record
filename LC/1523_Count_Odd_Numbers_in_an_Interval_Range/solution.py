# link of the problem: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low + 1) // 2 + (1 if low % 2 != 0 else 0)