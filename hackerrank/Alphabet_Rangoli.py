def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    total_width = (size * 2 - 1) * 2 - 1

    for i in range(size):
        current_letters = [alphabet[size - 1 - j] for j in range(i + 1)]
        
        left_part = "".join(current_letters)
        right_part = left_part[::-1][1:]
        
        center_string = left_part + right_part
        center_string_with_dash = "-".join(center_string)
        
        padding = (total_width - len(center_string_with_dash)) // 2
        line = '-' * padding + center_string_with_dash + '-' * padding
        
        lines.append(line)

    for line in lines:
        print(line)

    for i in range(len(lines) - 2, -1, -1):
        print(lines[i])

        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)