# link of the question: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for item in operations:
            if '+' in item:
                x += 1
            else:
                x -= 1

        return x