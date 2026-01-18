# link of the question: https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ans = 0
        min_r1, second_min_r1, min_r2, second_min_r2 = inf, inf, inf, inf
        for num in nums:
            ans += num
            if num % 3 == 1:
                if num < second_min_r1:
                    if num < min_r1:
                        second_min_r1 = min_r1
                        min_r1 = num
                    else:
                        second_min_r1 = num
            elif num % 3 == 2:
                if num < second_min_r2:
                    if num < min_r2:
                        second_min_r2 = min_r2
                        min_r2 = num
                    else:
                        second_min_r2 = num
            
        if ans % 3 == 0:
            return ans
        elif ans % 3 == 1:
            return max(ans - min_r1, ans - min_r2 - second_min_r2)
        else:
            return max(ans - min_r1 - second_min_r1, ans - min_r2)