import math

while True:
    try:
        radius = list(map(float, input().split()))
    except:
        break

    for i in range(len(radius)):
        striped_region = radius[i] * radius[i] * (math.pi / 3 - math.sqrt(3) + 1)
        dotted_region = 2 * radius[i] * radius[i] * (math.pi / 6 + math.sqrt(3) - 2)
        rest_region = 4 * radius[i] * radius[i] * (1 - math.pi / 6 - math.sqrt(3) / 4)
        
        print(f"{striped_region:.3f} {dotted_region:.3f} {rest_region:.3f}")
