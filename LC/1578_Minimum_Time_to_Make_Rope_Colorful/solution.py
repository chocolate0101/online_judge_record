# link of the question: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

# solution 1
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        i = 0
        while i < len(colors):
            repeat = i
            for j in range(i, len(colors)-1):
                if colors[j] == colors[j+1]:
                    repeat += 1
                else:
                    break
            total_time += sum(neededTime[i : repeat+1]) - max(neededTime[i : repeat+1])
            i = repeat + 1

        return total_time
    
# solution 2
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        previous = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[previous]:
                if neededTime[i] > neededTime[previous]:
                    total_time += neededTime[previous]
                    previous = i
                else:
                    total_time += neededTime[i]
            else:
                previous = i

        return total_time