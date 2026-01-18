# link of the question: https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/

class Solution:
    def totalMoney(self, n: int) -> int:
        complete_week = n // 7
        rest_day = n % 7
        total_money = 28 * complete_week

        for i in range(1, complete_week):
            total_money += 7 * i

        for i in range(1, rest_day+1):
            total_money += complete_week + i

        return total_money