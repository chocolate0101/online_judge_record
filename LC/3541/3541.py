# link of question: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
def maxFreqSum(self, s: str) -> int:
    vowel = {}
    consonant = {}
    for i in s:
        if i in 'aeiou':
            if i in vowel:
                vowel[i] += 1
            else:
                vowel[i] = 1
        else:
            if i in consonant:
                consonant[i] += 1
            else:
                consonant[i] = 1

    max_vowel_value = max(vowel.values()) if vowel else 0
    max_consonant_value = max(consonant.values()) if consonant else 0
    return max_vowel_value + max_consonant_value