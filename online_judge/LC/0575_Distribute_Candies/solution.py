# link of the question: https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candy_type = set(candyType)
        if len(unique_candy_type) <= len(candyType) / 2:
            return len(unique_candy_type)
        else:
            return len(candyType) // 2