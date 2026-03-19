cases = int(input())

for i in range(cases):
    start = int(input())
    end = int(input())
    total = 0

    for j in range(start, end+1):
        if j % 2 == 0:
            continue
        else:
            total += j

    print(f"Case {i+1}: {total}")