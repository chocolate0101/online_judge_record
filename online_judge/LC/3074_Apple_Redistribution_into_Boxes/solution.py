# link of the problem: https://leetcode.com/problems/apple-redistribution-into-boxes/description/

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)
        capacity.sort(reverse=True)
        count = 0
        while total_apple > 0:
            total_apple -= capacity[count]
            count += 1

        return count