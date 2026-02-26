class Solution:
    def numSteps(self, s: str) -> int:
        total_step = 0
        num = int(s, 2)
        while num != 1:
            if num % 2 == 0:
                num >>= 1
            else:
                num += 1

            total_step += 1

        return total_step
