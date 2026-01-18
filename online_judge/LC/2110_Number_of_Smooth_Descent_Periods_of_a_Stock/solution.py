# link of the problem: https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 0
        smooth_descent_count = 1
        for i in range(len(prices)-1):
            if prices[i] - 1 == prices[i+1]:
                smooth_descent_count += 1
            else:
                tmp = smooth_descent_count * (smooth_descent_count + 1) // 2
                smooth_descent_count = 1
                count += tmp
        
        tmp = smooth_descent_count * (smooth_descent_count + 1) // 2
        smooth_descent_count = 1
        count += tmp
        
        return count