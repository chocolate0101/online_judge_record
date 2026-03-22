output_list = []
mapping_table = {'W': 'Q', 'E': 'W', 'R': 'E', 'T': 'R', 'Y': 'T',
                    'U': 'Y', 'I': 'U', 'O': 'I', 'P': 'O', '[': 'P',
                    'S': 'A', 'D': 'S', 'F': 'D', 'G': 'F', 'H': 'G',
                    'J': 'H', 'K': 'J', 'L': 'K', ';': 'L', 'X': 'Z',
                    'C': 'X', 'V': 'C', 'B': 'V', 'N': 'B', 'M': 'N',
                    ',': 'M', '2': '1', '3': '2', '4': '3', '5': '4',
                    '6': '5', '7': '6', '8': '7', '9': '8', '0': '9',
                    '-': '0', '=': '-', ']': '[', '/': '.', '\\': ']',
                    '1': '`', '\'': ';', '.': ','}

while True:
    try:
        strings = input()
    except:
        break

    output = ""
    for ch in strings:
        if ch == " ":
            output += " "
        else:
            output += mapping_table[ch]

    output_list.append(output)

print("\n".join(output_list))