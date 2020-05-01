# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

#Using the facts that a < b < c, and thus exploiting  a < s/3,  and a < b < s/2.
from math import *;

def triplet():
    c = 1
    s = 1000
    for i in range (1,ceil(s/3)): #i is a and j is b here.
        for j in range(i+1,ceil(s/2)): # b should be more than a.
            c = s - i - j # we know a + b + c = 1000
            if(((pow(i,2)) + (pow(j,2))) == (pow(c,2))):
                print(i)
                print(j)
                print(c)
                prod = i * j * c
                return prod

print(triplet())
