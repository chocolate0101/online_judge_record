# link of the question: https://leetcode.com/problems/1-bit-and-2-bit-characters/description/

# solution 1
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True
        n = 0
        while n < len(bits):
            if bits[n] == 1:
                n += 2
            else:
                n += 1
            
            if n == len(bits)-1:
                return True
        
        return False

# solution 2
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return i == len(bits) - 1