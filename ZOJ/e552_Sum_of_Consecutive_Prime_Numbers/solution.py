# link of the question: https://zerojudge.tw/ShowProblem?problemid=e552

def is_prime_table() -> list[int]:
    is_prime_number = [ True for _ in range(10001)]
    is_prime_number[0], is_prime_number[1] = False, False

    for i in range(2, len(is_prime_number)):
        if is_prime_number[i]:
            for j in range(i*i, len(is_prime_number), i):
                is_prime_number[j] = False

    return is_prime_number


is_prime_number = is_prime_table()

while True:
    num = int(input())
    if num == 0:
        break

    count = 0
    for i in range(2, num+1):
        if is_prime_number[i]:
            sum = 0
            for j in range(i, num+1):
                if is_prime_number[j]:
                    sum += j
                    if sum == num:
                        count += 1
                        break
                    elif sum > num:
                        break
    print(count)