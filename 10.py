# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

#The bruteforce way.
#First we need to check if the number is prime or not.
#Once we find the number is prime add the number to a temp number assigned as 0 initially.

# def prime(a):
#     for i in range(2,a):
#         if((a % i) == 0):
#             return 0
#     return a
#
# def add_p():
#     a = 3
#     sum = 2
#     start = 1
#     while(a < 100):
#         c = prime(a)
#         if(c != 0):
#             sum +=c
#             #print(sum)
#
#             a +=1
#         else:
#             a +=1
#
#     print(sum)
#
# add_p()

#Using SieveOfEratosthenes:

def SieveOfEratosthenes(n):

    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)] # This has all boolean values.
    p = 2
    num =0
    while (p * p <= n):# this will cehck condition .

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            num +=p
    print(num)


n = 2000000
print( "Following are the prime numbers smaller",)
print ("than or equal to", n)
SieveOfEratosthenes(n)
