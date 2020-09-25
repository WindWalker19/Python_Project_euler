# The sum of the squares of the first ten natural numbers is,
#
# 12+22+...+102=385
# 1
# 2
# +
# 2
# 2
# +
# .
# .
# .
# +
# 10
# 2
# =
# 385
# The square of the sum of the first ten natural numbers is,
#
# (1+2+...+10)2=552=3025
# (
# 1
# +
# 2
# +
# .
# .
# .
# +
# 10
# )
# 2
# =
# 55
# 2
# =
# 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
# 3025
# −
# 385
# =
# 2640
# .
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def diff_sum(n):
    sum_sq = 0
    sum = 0
    for i in range (1,n+1):
        sum_sq = sum_sq + pow(i,2)
        sum = sum + i
    diff = pow(sum,2) - sum_sq
    print(diff)

diff_sum(100)


#Using while loop.

import math

def sum_diff(num):

    i = 1
    square_sum = 0
    sum = 0
    while (i <= num):
        #sum of the first 100 natural .
        sum +=i
        #sum of the square of first 100 natural number.
        square_sum += pow(i,2)
        i +=1
    #sum of the first 100 natural number square.
    # pow(sum,2)
    # #sum of the square of first 100 natural number.
    # square_sum
    diff = (pow(sum,2)) - square_sum
    return (diff)

print(sum_diff(100))
