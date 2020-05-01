#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time;
from math import *;


def small_num_div():
    n = 10
    while(True):
        if((n%2 == 0)and(n%3 == 0)and(n%4 == 0)and(n%5 == 0)and(n%6 == 0)and(n%7 == 0)and(n%8 == 0)and(n%9 == 0)and(n%10 == 0)and(n%11 == 0)and(n%12 == 0)and(n%13 == 0)and(n%14 == 0)and(n%15 == 0)and(n%16 == 0)and(n%17 == 0)and(n%18 == 0)and(n%19 == 0)and(n%20 == 0)):
            return n
        else:
            n += 1




# start_time = time.time()
# # print(small_num_div())
# print("--- %s seconds ---" % (time.time() - start_time))



# Returns the lcm of first n numbers
def lcm(n):
    ans = 1
    for i in range(1, n + 1):
        ans = int((ans * i)/gcd(ans, i))
    return ans

# main
n = 20
print (lcm(n))

# def ifDividesAll(num):
#     for i in range(2,21):
#         if num % i != 0:
#             return False
#     return True
#
# def hi():
#     num = 20
#     while True:
#         if ifDividesAll(num):
#             break
#         else:
#             num = num + 1
#
#     print (num)
#
# hi()
