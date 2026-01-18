# link of the question: https://leetcode.com/problems/smallest-number-with-all-set-bits/description/

# solution 1
class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(n+1):
            if ((2 ** i) - 1) >= n:
                return 2 ** i - 1
            
# solution 2
class Solution:
    def smallestNumber(self, n: int) -> int:
        i = 1
        while i <= n:
            i *= 2
        return i-1
    
# solution 3
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1