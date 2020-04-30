# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def lpal(a,b):
    lpal = 0
    for i in range (a,900,-1):
        for j in range (b,900,-1):
            prod = str(i * j)
            rprod = prod[::-1]
            num = int(prod)
            if((prod == rprod) and (lpal < num)):
                prod = int(rprod)
                lpal = prod
    print(lpal)

lpal(999,999)
