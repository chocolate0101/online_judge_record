# link of the problem: https://leetcode.com/problems/count-square-sum-triples/

class Solution:
    def countTriples(self, n: int) -> int:
        square_sum = set( _ ** 2 for _ in range(1, n+1))
        count = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if (i ** 2 + j ** 2) in square_sum:
                    count += 1

        return count