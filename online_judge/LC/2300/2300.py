# link of the question: https://leetcode.com/problems/successful-pairs-of-spells-and-potions

# better approach
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for i in spells:
            threshold = (success + i - 1) // i
            start = 0
            end = len(potions)
            count = 0
            while start < end:
                mid = start + (end - start) // 2
                if threshold > potions[mid]:
                    start = mid + 1
                else:
                    end = mid
            
            count = len(potions) - start
            ans.append(count)
                
        return ans

# brute force
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort(reverse=True)
        is_early_break = 0
        ans = []
        for i in spells:
            count = 0
            for j in potions:
                if i*j >= success:
                    count += 1
                else:
                    ans.append(count)
                    is_early_break = 1
                    break
            if is_early_break:
                is_early_break = 0
            else:
                ans.append(count)

        return ans