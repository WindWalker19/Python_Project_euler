# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

# def prime_pos(b):
#     a = 3
#     counter = 1
#     while(counter!=b):
#         for i in range(2,a):
#             if(a%i == 0):
#                 a +=1
#
#         counter +=1
#         a +=1
#
#     print(a - 1)
#     print(counter)
#
# prime_pos(10)
#
def prime(a):
    for i in range (2,a):
        if((a%i) == 0):
            return False
    return True

counter = 1
a = 3
while(counter != 10001):
    if(prime(a) == True):
        counter+=1
        a+=1
    else:
        a+=1
print(a-1)
