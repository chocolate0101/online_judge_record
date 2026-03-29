while 1:
    try:
        input_list = list(map(int, input().split()))
    except:
        break
    
    for i in range(0, len(input_list), 2):
        n = input_list[i]
        m = input_list[i+1]
        
        if m == 0 or n == 0:
            print(0)
        else:
            period = 3 * (1 << (m-1))
            n %= period
            module = 1 << m

            prev = 0
            prev_prev = 1
            cur = 1
            for _ in range(n):
                cur = (prev + prev_prev) % module
                prev_prev = prev
                prev = cur

            print(cur)