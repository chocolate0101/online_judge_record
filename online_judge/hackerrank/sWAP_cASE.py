# link of the question：https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    after_swapcase = s.swapcase()
    return after_swapcase

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)