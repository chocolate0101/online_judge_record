# link of the question: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

# first try
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False
        
        str_2_int = [ int(_) for _ in s]
        
        while(1):
            new_str = []
            for i in range(len(str_2_int)-1):
                new_str.append( (str_2_int[i] + str_2_int[i+1]) % 10)

            if len(new_str) == 2:
                if new_str[0] == new_str[1]:
                    return True
                else:
                    return False
                
            str_2_int = new_str

# more clear on writing
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        str_2_int = [ int(_) for _ in s]
        while len(str_2_int) > 2:
            new_str = []
            for i in range(len(str_2_int)-1):
                new_str.append( (str_2_int[i] + str_2_int[i+1]) % 10)
                
            str_2_int = new_str

        return str_2_int[0] == str_2_int[1]