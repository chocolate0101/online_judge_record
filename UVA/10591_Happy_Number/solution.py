import math

cases = int(input())

for i in range(1, cases+1):
    num = int(input())

    tmp = num
    record = {tmp}
    while 1:
        square_sum = 0
        while tmp > 0:
            square_sum += int(math.pow(tmp % 10, 2))
            tmp //= 10

        if square_sum == 1:
            print(f"Case #{i}: {num} is a Happy number.")
            break
        elif square_sum in record:
            print(f"Case #{i}: {num} is an Unhappy number.")
            break
        else:
            record.add(square_sum)

        tmp = square_sum