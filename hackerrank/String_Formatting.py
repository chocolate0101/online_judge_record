def print_formatted(number):
    space_length = len(bin(number)[2:])
    for i in range(1, number+1):
        decimal = i
        octal = f"{i:o}"
        hexadecimal = f"{i:X}"
        binary = f"{i:b}"
        print(f"{decimal:>{space_length}} {octal:>{space_length}} {hexadecimal:>{space_length}} {binary:>{space_length}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)