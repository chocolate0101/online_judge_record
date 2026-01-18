# link of the question:https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        num_empty_bottle = numBottles
        max_bottle = numBottles
        while True:
            if num_empty_bottle < numExchange:
                return max_bottle
            else:
                num_change = num_empty_bottle // numExchange
                num_empty_bottle = num_empty_bottle - num_change * numExchange + num_change
                max_bottle += num_change