# solution 1 (Greedy)
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        max_value = 0
        for i in range(k):
            tmp = happiness[i] - i
            if tmp <= 0:
                break
            max_value += tmp

        return max_value
    
# solution 2 (min-heap)
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k:int) -> int:
        top_k_happiness = heapq.nlargest(k, happiness)

        max_value = 0
        for i in range(k):
            tmp = top_k_happiness[i] - i
            if tmp <= 0:
                break
            max_value += tmp

        return max_value