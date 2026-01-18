# link of the question: https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

import cmath

complex_num = complex(input())
magnitude, argument = cmath.polar(complex_num)

print(magnitude)
print(argument)