import math

while 1:
    try:
        l, w = map(int, input().split())
    except:
        break

    tmp = math.pow(l, 2) + math.pow(w, 2) - l * w
    x = ((l + w) - math.sqrt(tmp)) / 6
    min_1 = min(l, w) / 2

    print(f"{x:.3f} 0.000 {min_1:.3f}")

