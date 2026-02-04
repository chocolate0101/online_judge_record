# solution 1
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
            
        return letters[0]

# solution 2
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i, j, mid = 0, len(letters)-1, 0

        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        while i <= j:
            mid = (i + j) // 2
            if letters[mid] <= target:
                i = mid + 1
            elif letters[mid] > target:
                j = mid - 1
        
        return letters[i]