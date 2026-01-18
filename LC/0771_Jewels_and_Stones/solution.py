# link of the question: https://leetcode.com/problems/jewels-and-stones

# solution 1
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total_jewel = 0
        for chr in stones:
            if chr in jewels:
                total_jewel += 1

        return total_jewel
    
# solution 2
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(i in jewel_set for i in stones)

# solution 3
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_count = Counter(stones) # if not write in leetcode environment, need to import Counter (from collections import Counter)
        total_jewel = 0

        for jewel in jewels:
            total_jewel += stone_count[jewel]

"""
- time complexity of solution 1: O(J * S)
    J = length of the jewels
    S = length of the stones

    because you pick up all of the characters in stones and check if it is in jewels or not

- time complexity of solution 2: O(J + S)
    change the jewels to a set (jewel_set) need to iterate all the characters in jewels => O(J)
    pick up all of the characters in stones and check if it is in jewel_set => O(S) * O(1)
    set can check the element average time in O(1)
    therefore, total = O(J) + O(S) * O(1) = O(J+S)

- time complexity of solution 3: O(S + J)
    using the Counter will count all the element in stones => O(S)
    pick up all the characters in jewels and check if it is in stone_count => O(J) * O(1)
    Counter can check the element average time in O(1)
    therefore, total = O(S) + O(J) * O(1) = O(S + J)
"""

"""
- space complexity of solution 1: O(1)
    it only takes one variable (total_jewel) to count

- space complexity of solution 2: O(J)
    create a set (jewel_set) to store the different jewel in jewels
    in the worst case, the jewels' element is all different
    at this case, the length of the jewel_set will be J
    so the space complexity will be O(J)

- space complexity of solution 3: O(S)
    create a Counter (stone_count) to count the appear number of each different stone in stones
    in the worst case, the stones' element is all different
    at this case, the length of the stone_count will be S
    so the space complexity will be O(S)
"""

"""
- Counter
    Counter is specifically for counting.
    
    It will make a dictionary so it can have all the function that dictionary has.
    Ex: {'s': 1, 'e': 2}
    
    key is the item that you want to count
    value is the number of item that been found
    
    when you try to access the key that is not in Counter
    it won't make a KeyError like traditional dictionary
    it will return 0
    this is convenient for counting

Ex: c = Counter(['apple', 'banana', 'apple'])
using [] to get the value for the item that you want
c['apple'] => 2
c['banana'] => 1
c['guava'] => 0 (won't get KeyError)
"""
