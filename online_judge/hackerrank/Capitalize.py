import os

def solve(s):
    is_new_word = 1
    result = []
    for ch in s:
        if ch == " ":
            is_new_word = 1
            result.append(ch)
        elif not ch.isalpha():
            result.append(ch)
            is_new_word = 0
        else:
            if is_new_word:
                result.append(ch.upper())
                is_new_word = 0
            else:
                result.append(ch)
            
    return "".join(result)

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)