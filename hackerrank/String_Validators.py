# link of the question：https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

if __name__ == '__main__':
    s = input()
    is_alnum = 0
    is_alpha = 0
    is_digit = 0
    is_lower = 0
    is_upper = 0
    
    for i in range(len(s)):
        if s[i].isalnum():
            is_alnum = 1
            print("True")
            break
    if not is_alnum:
        print("False")
    
    for i in range(len(s)):
        if s[i].isalpha():
            is_alpha = 1
            print("True")
            break
    if not is_alpha:
        print("False")
    
    for i in range(len(s)):
        if s[i].isdigit():
            is_digit = 1
            print("True")
            break
    if not is_digit:
        print("False")
    
    for i in range(len(s)):
        if s[i].islower():
            is_lower = 1
            print("True")
            break
    if not is_lower:
        print("False")
    
    for i in range(len(s)):
        if s[i].isupper():
            is_upper = 1
            print("True")
            break
    if not is_upper:
        print("False")