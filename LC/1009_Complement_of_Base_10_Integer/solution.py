class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary_n = bin(n)[2:]
        ans = 0
        for ch in binary_n:
            ans *= 2
            if ch == '0':
                ans += 1
            
        return ans