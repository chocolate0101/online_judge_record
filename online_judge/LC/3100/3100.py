# link of the question: https://leetcode.com/problems/water-bottles-ii/

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drink = numBottles
        empty_bottle = numBottles
        while empty_bottle >= numExchange:
            empty_bottle = empty_bottle - numExchange + 1
            numExchange += 1
            total_drink += 1
        return total_drink