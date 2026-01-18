# link of the problem: https://leetcode.com/problems/fair-candy-swap/description/

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_set = set(aliceSizes)
        bob_set = set(bobSizes)
        total_alice = sum(aliceSizes)
        total_bob = sum(bobSizes)
        for alices in alice_set:
            bobs = (total_bob + 2 * alices - total_alice) / 2
            if bobs in bob_set:
                return [alices, bobs]