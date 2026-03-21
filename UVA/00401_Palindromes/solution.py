while True:
    try:
        string = input()
    except:
        break

    is_palindromes =  True
    is_mirror = True
    length = len(string)

    reversed_table =   {'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J',
                        'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V',
                        'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', '1': '1', '2': 'S',
                        '3': 'E', '5': 'Z', '8': '8'}
    
    for i in range(length):
        if is_palindromes and string[i] != string[length - i - 1]:
            is_palindromes = False

        if is_mirror:
            if string[i] in reversed_table:
                if string[length - i - 1] != reversed_table[string[i]]:
                    is_mirror = False
            else:
                is_mirror = False
            
        if not is_palindromes and not is_mirror:
            break

    if is_mirror and is_palindromes:
        print(f"{string} -- is a mirrored palindrome.")
    elif not is_mirror and is_palindromes:
        print(f"{string} -- is a regular palindrome.")
    elif is_mirror and not is_palindromes:
        print(f"{string} -- is a mirrored string.")
    else:
        print(f"{string} -- is not a palindrome.")

    print()
