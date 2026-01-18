# link of the question: https://leetcode.com/problems/ones-and-zeroes/description/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        str_counter = []
        for s in strs:
            str_counter.append([s.count('0'), s.count('1')])
            
        dp = [[0 for i in range(n+1)] for i in range(m+1)]

        for str_count in str_counter:
            zero = str_count[0]
            one = str_count[1]
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    if zero <= i and one <= j:
                        dp[i][j] = max(dp[i][j], dp[i-zero][j-one]+1)

        return dp[m][n]
            