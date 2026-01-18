// link of the question: https://leetcode.com/problems/water-bottles-ii/

class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int total_drink = numBottles;
        int empty_bottle = numBottles;

        while (empty_bottle >= numExchange) {
            empty_bottle = empty_bottle - numExchange + 1;
            numExchange++;
            total_drink++;
        }

        return total_drink;
    }
};