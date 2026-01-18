class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int num_empty_bottle = numBottles;
        int total_drink = numBottles;
        while (num_empty_bottle >= numExchange) {
            int num_change = num_empty_bottle / numExchange;
            total_drink += num_change;
            num_empty_bottle = num_empty_bottle - num_change * numExchange + num_change;
        }

        return total_drink;
    }
};