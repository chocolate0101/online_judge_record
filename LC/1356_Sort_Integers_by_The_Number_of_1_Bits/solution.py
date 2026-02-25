class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans = []
        for num in arr:
            count = bin(num).count('1')
            ans.append([count, num])

        ans.sort()

        return [num[1] for num in ans]